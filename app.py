# StudioX Cloud Pro - Final Version (Free Mode + Optional OpenAI)
import os, io, uuid, shutil, time, base64
from typing import Optional
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, "assets", "output")
BGM_DIR = os.path.join(BASE_DIR, "assets", "bgm")
STORIES_DIR = os.path.join(BASE_DIR, "assets", "stories")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(BGM_DIR, exist_ok=True)
os.makedirs(STORIES_DIR, exist_ok=True)

app = FastAPI(title="StudioX Cloud Pro")

DIST_DIR = os.path.join(BASE_DIR, "frontend", "dist")
if os.path.isdir(DIST_DIR):
    app.mount("/static", StaticFiles(directory=os.path.join(DIST_DIR, "assets")), name="static")
    @app.get('/', include_in_schema=False)
    def root():
        return FileResponse(os.path.join(DIST_DIR, "index.html"))
else:
    @app.get('/')
    def no_frontend():
        return {"error":"Frontend not found. Please upload frontend/dist or build before deploying."}

class GenerateReq(BaseModel):
    title: Optional[str] = "Untitled"
    story: str
    aspect: Optional[str] = "landscape"
    bgm: Optional[str] = None
    use_openai: Optional[bool] = True

JOB_STORE = {}

@app.get("/api/bgms")
def api_bgms():
    files = [f for f in os.listdir(BGM_DIR) if f.endswith('.mp3')]
    return {"bgms": files}

@app.post("/api/generate")
def generate(req: GenerateReq, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    JOB_STORE[job_id] = {"status": "queued", "title": req.title}
    background_tasks.add_task(job_worker, job_id, req.title, req.story, req.aspect, req.bgm, req.use_openai)
    return {"job_id": job_id}

@app.get("/api/status/{job_id}")
def status(job_id: str):
    return JOB_STORE.get(job_id, {"error": "job not found"})

@app.get("/api/download/{job_id}")
def download(job_id: str):
    info = JOB_STORE.get(job_id)
    if not info or info.get("status") != "done":
        raise HTTPException(status_code=400, detail="not ready")
    return FileResponse(info["file"], filename=os.path.basename(info["file"]), media_type="video/mp4")

def generate_placeholder_image(text, w, h):
    img = Image.new("RGB", (w, h), "#071226")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((20, h // 3), text[:100], fill="white", font=font)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

def job_worker(job_id, title, story, aspect, bgm, use_openai):
    JOB_STORE[job_id]["status"] = "started"
    try:
        scenes = story.split("\n")
        size = (1280, 720) if aspect == "landscape" else (720, 1280)
        image_paths = []
        for idx, scene in enumerate(scenes[:5]):
            buf = generate_placeholder_image(scene, *size)
            img_path = os.path.join(OUTPUT_DIR, f"{job_id}_{idx}.png")
            with open(img_path, "wb") as f:
                f.write(buf.read())
            image_paths.append(img_path)
        audio_path = os.path.join(OUTPUT_DIR, f"{job_id}.mp3")
        gTTS(story, lang="en", tld="co.in").save(audio_path)
        out_path = os.path.join(OUTPUT_DIR, f"{job_id}.mp4")
        clips = [ImageClip(p).set_duration(3) for p in image_paths]
        video = concatenate_videoclips(clips)
        narration = AudioFileClip(audio_path)
        video = video.set_audio(narration)
        video.write_videofile(out_path, fps=24, codec="libx264", audio_codec="aac", verbose=False, logger=None)
        JOB_STORE[job_id].update({"status": "done", "file": out_path})
    except Exception as e:
        JOB_STORE[job_id].update({"status": "error", "error": str(e)})
