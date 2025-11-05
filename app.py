from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

@app.get("/api/sample")
def sample():
    return {"message": "StudioX Cloud API is active.", "sample_story": "The Pebble Path - Rise of Anu"}

DIST_DIR = os.path.join(os.path.dirname(__file__), "frontend", "dist")

if os.path.isdir(DIST_DIR):
    app.mount("/static", StaticFiles(directory=os.path.join(DIST_DIR, "assets")), name="static")

    @app.get("/", include_in_schema=False)
    def root():
        return FileResponse(os.path.join(DIST_DIR, "index.html"))

    @app.get("/{full_path:path}", include_in_schema=False)
    def spa(full_path: str, request: Request):
        if request.url.path.startswith("/api"):
            return JSONResponse(status_code=404, content={"detail": "Not Found"})
        return FileResponse(os.path.join(DIST_DIR, "index.html"))
else:
    @app.get("/")
    def root_no_frontend():
        return {"error": "Frontend not found. Please build and redeploy."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
