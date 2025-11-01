from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="StudioX Cloud")

# --- API routes ---
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

@app.get("/api/sample")
def sample():
    return {
        "message": "StudioX Cloud API is active.",
        "sample_story": "The Pebble Path - Rise of Anu"
    }

# --- Serve built frontend ---
BASE_DIR = os.path.dirname(__file__)
DIST_DIR = os.path.join(BASE_DIR, "frontend", "dist")

if os.path.exists(DIST_DIR):
    app.mount(
        "/assets",
        StaticFiles(directory=os.path.join(DIST_DIR, "assets")),
        name="assets"
    )

    @app.get("/", include_in_schema=False)
    async def serve_root():
        return FileResponse(os.path.join(DIST_DIR, "index.html"))

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(full_path: str, request: Request):
        if request.url.path.startswith("/api"):
            return JSONResponse(status_code=404, content={"detail": "Not Found"})
        return FileResponse(os.path.join(DIST_DIR, "index.html"))
else:
    @app.get("/", include_in_schema=False)
    async def frontend_missing():
        return {
            "error": "Frontend not found. Please build with 'npm run build' inside /frontend and redeploy."
        }

# --- Main entrypoint ---
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
