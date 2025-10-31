from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# ✅ Serve frontend static files
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend", "public")
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
else:
    @app.get("/")
    async def frontend_not_found():
        return {"error": "Frontend not found. Please rebuild the app."}

# ✅ Health check route
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
