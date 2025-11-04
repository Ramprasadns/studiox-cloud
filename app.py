from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os, json, random

app = FastAPI(title="StudioX Cloud")

@app.get('/api/health')
def health():
    return {'status':'ok','service':'studiox-backend'}

@app.get('/api/sample')
def sample():
    # return a random sample story title
    stories_dir = os.path.join(os.path.dirname(__file__), 'assets', 'stories')
    stories = []
    if os.path.isdir(stories_dir):
        for f in os.listdir(stories_dir):
            if f.endswith('.json'):
                with open(os.path.join(stories_dir, f), 'r', encoding='utf-8') as fh:
                    stories.append(json.load(fh))
    if stories:
        s = random.choice(stories)
        return {'message':'AI Narration Preview Ready','sample_story':s.get('title','Untitled')}
    return {'message':'No stories found','sample_story':None}

# Serve frontend
DIST_DIR = os.path.join(os.path.dirname(__file__), 'frontend', 'dist')
if os.path.isdir(DIST_DIR):
    static_dir = os.path.join(DIST_DIR, 'assets')
    if os.path.isdir(static_dir):
        app.mount('/static', StaticFiles(directory=static_dir), name='static')

    @app.get('/', include_in_schema=False)
    def root():
        return FileResponse(os.path.join(DIST_DIR, 'index.html'))

    @app.get('/{full_path:path}', include_in_schema=False)
    def spa(full_path: str, request: Request):
        if request.url.path.startswith('/api'):
            return JSONResponse(status_code=404, content={'detail':'Not Found'})
        return FileResponse(os.path.join(DIST_DIR, 'index.html'))
else:
    @app.get('/')
    def no_frontend():
        return {'error':'Frontend not found. Please upload frontend/dist or build before deploying.'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
