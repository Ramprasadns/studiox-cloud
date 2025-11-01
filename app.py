from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os

app = FastAPI(title="StudioX Cloud", version="1.0")

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend files
frontend_dir = os.path.join(os.getcwd(), "frontend", "public")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

# Health check
@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "studiox-backend"}

# Placeholder API for demo
@app.get("/api/sample")
def sample_story():
    stories = [
        {"title": "The Pebble Path", "message": "Click Generate to create a sample video"},
        {"title": "Rise of Anu", "message": "An inspiring tale of courage and self-belief."},
        {"title": "The Box of Dreams", "message": "A magical journey of imagination."}
    ]
    return JSONResponse(content={"stories": stories})
