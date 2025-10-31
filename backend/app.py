# Placeholder backend for StudioX Cloud (FastAPI)
from fastapi import FastAPI
app = FastAPI()
@app.get('/api/health')
def health():
    return {'status':'ok','service':'studiox-backend'}
