# StudioX Cloud — Quick Setup Guide

1. Create a GitHub repo named `studiox-cloud` and upload the extracted files to the root.
2. Sign into Vercel with GitHub (use ramaigen2025@gmail.com).
3. Import the repo into Vercel as a new project.
4. Set environment variables in Vercel (Project Settings → Environment Variables):
   - STUDIOX_ADMIN_EMAIL=ramaigen2025@gmail.com
   - DEFAULT_STORY=The Pebble Path
   - PROJECT_MODE=cloud
   - (Optional) NANOBANANA_API_KEY, VOICE_API_KEY, WHISPER_API_KEY
5. Deploy. After deployment, visit the project URL and open `/api/health` to verify backend health.
6. To preview locally, run `run_local.bat` (Windows) or `run_local.sh` (macOS/Linux) and open http://localhost:8000.
