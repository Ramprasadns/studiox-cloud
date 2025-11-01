from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
app=FastAPI()
@app.get('/api/health')
def health():
    return {'status':'ok','service':'studiox-backend'}
DIST_DIR=os.path.join(os.path.dirname(__file__),'frontend','dist')
if os.path.isdir(DIST_DIR):
    app.mount('/static', StaticFiles(directory=os.path.join(DIST_DIR,'assets')), name='static')
    @app.get('/')
    def root():
        return FileResponse(os.path.join(DIST_DIR,'index.html'))
else:
    @app.get('/')
    def no_front():
        return {'error':'Frontend not found. Please build the frontend (npm run build) and redeploy.'}
