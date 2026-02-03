# Django TemplateDoesNotExist Error - Resolution

## Problem
Django was throwing a `TemplateDoesNotExist` error for `index.html` because the frontend React application had not been built yet. The error occurred at:
```
TemplateDoesNotExist at /
index.html
```

Django was looking for the file at: `C:\Users\prabu\Downloads\SRUSHTI\frontend\dist\index.html` but the `dist` folder was empty.

## Root Cause
This is a Django + React/Vite application where:
1. The frontend is a separate React application built with Vite
2. Django serves the built frontend files from `frontend/dist/`
3. The frontend had never been built, so the `dist/` directory was empty

## Solution Implemented

### 1. Updated Vite Configuration (`frontend/vite.config.js`)
Added build configuration to ensure proper integration with Django:
```javascript
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: './index.html',
    },
  },
  base: '/static/',
})
```

### 2. Built the Frontend Application
Ran the build command to generate production files:
```bash
cd frontend
npm run build
```

This created:
- `frontend/dist/index.html`
- `frontend/dist/assets/` (CSS and JS files)
- `frontend/dist/.vite/manifest.json`

### 3. Updated Django URL Configuration (`content_planner/urls.py`)
Added API routes that were missing:
```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("content_posts.urls")),  # Added API routes
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
```

## Verification
The Django development server now runs successfully and serves:
- Frontend React app at: `http://127.0.0.1:8000/`
- API endpoints at: `http://127.0.0.1:8000/api/`
- Admin panel at: `http://127.0.0.1:8000/admin/`

## Future Deployments

### Development Workflow
1. Make changes to frontend code in `frontend/src/`
2. Rebuild the frontend: `cd frontend && npm run build`
3. Django will automatically serve the updated files

### Production Deployment
Ensure the build step is included in your deployment process:
```bash
# Install frontend dependencies
cd frontend
npm install

# Build the frontend
npm run build

# Collect static files for Django
cd ..
python manage.py collectstatic --noinput
```

## Notes
- The frontend build outputs to `frontend/dist/` which is configured in Django's `TEMPLATES['DIRS']` and `STATICFILES_DIRS`
- Static files are served with WhiteNoise middleware
- The API base URL is configured in `frontend/src/services/api.js` as `http://localhost:8000/api`
