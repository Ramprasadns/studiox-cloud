# StudioX Cloud — Unified Backend + Frontend (FastAPI)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# ✅ Health Check
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

# ✅ Serve built frontend
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend", "dist")

if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")

# ✅ Optional: React Router support (fallback to index.html)
@app.get("/{full_path:path}")
def serve_frontend(full_path: str):
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Frontend not found. Please rebuild the app."}

# ✅ Local run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
