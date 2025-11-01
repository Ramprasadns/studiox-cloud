from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="StudioX Cloud")

# Serve frontend files
frontend_dir = os.path.join(os.getcwd(), "frontend", "public")
app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")

@app.get("/")
async def root():
    index_path = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse({"error": "Frontend not found"}, status_code=404)

# ✅ Health check route
@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "studiox-backend"}

# ✅ Sample data route
@app.get("/api/sample")
async def sample():
    return {
        "message": "StudioX Cloud API is active.",
        "sample_story": "The Pebble Path - Rise of Anu"
    }

# Run locally (Render will call via CMD)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
