from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# --- API routes ---
@app.get('/api/health')
def health():
    return {'status':'ok','service':'studiox-backend'}

@app.get('/api/sample')
def sample():
    return {"message":"StudioX Cloud API is active.","sample_story":"The Pebble Path - Rise of Anu"}

# --- Serve built frontend ---
DIST_DIR = os.path.join(os.path.dirname(__file__), 'frontend', 'dist')

if os.path.isdir(DIST_DIR):
    app.mount("/static", StaticFiles(directory=os.path.join(DIST_DIR, 'assets')), name="static")
    @app.get("/", include_in_schema=False)
    def root():
        index_path = os.path.join(DIST_DIR, "index.html")
        return FileResponse(index_path)

    @app.get("/{full_path:path}", include_in_schema=False)
    def spa(full_path: str, request: Request):
        # Return index.html for client-side routing unless the path begins with /api
        if request.url.path.startswith('/api'):
            return JSONResponse(status_code=404, content={"detail":"Not Found"})
        index_path = os.path.join(DIST_DIR, "index.html")
        return FileResponse(index_path)
else:
    # if no dist (dev mode on Render before build), simple root
    @app.get("/")
    def root_no_frontend():
        return {"error":"Frontend not found. Please build the frontend (npm run build) and redeploy."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
