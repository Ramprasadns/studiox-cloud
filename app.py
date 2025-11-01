from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="StudioX Cloud Backend", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static frontend files
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend", "public")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
else:
    @app.get("/")
    async def missing_frontend():
        return JSONResponse({"error": "Frontend not found. Please rebuild the app."})

# Health check endpoint
@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "studiox-backend"}

# Root API info
@app.get("/api/info")
async def info():
    return {
        "name": "StudioX Cloud",
        "version": "1.0",
        "description": "AI Voice & Video Narration Studio",
    }

# Optional test route
@app.get("/api/test")
async def test():
    return {"message": "Backend is running perfectly ✅"}
