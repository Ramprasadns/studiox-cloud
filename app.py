from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydub import AudioSegment
from gtts import gTTS
import os

app = FastAPI()

# Serve static frontend
app.mount("/", StaticFiles(directory="frontend/public", html=True), name="frontend")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

@app.post("/api/tts")
async def text_to_speech(text: str = Form(...)):
    """Convert text to speech using gTTS."""
    os.makedirs("assets/output", exist_ok=True)
    file_path = f"assets/output/output.mp3"
    tts = gTTS(text)
    tts.save(file_path)
    return FileResponse(file_path, media_type="audio/mpeg")

@app.post("/api/merge")
async def merge_audio_video(audio: UploadFile, video: UploadFile):
    """Merge uploaded audio and video into one output file."""
    os.makedirs("assets/output", exist_ok=True)
    audio_path = f"assets/output/{audio.filename}"
    video_path = f"assets/output/{video.filename}"
    out_path = "assets/output/final.mp4"

    with open(audio_path, "wb") as f:
        f.write(await audio.read())
    with open(video_path, "wb") as f:
        f.write(await video.read())

    from moviepy.editor import VideoFileClip, AudioFileClip
    clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final = clip.set_audio(audio_clip)
    final.write_videofile(out_path, codec="libx264", audio_codec="aac")

    return FileResponse(out_path, media_type="video/mp4")
