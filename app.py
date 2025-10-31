# StudioX Cloud — Unified FastAPI backend + static frontend
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# API route
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studiox-backend"}

# Serve static frontend files
app.mount("/", StaticFiles(directory="frontend/public", html=True), name="static")

# Local entry
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
