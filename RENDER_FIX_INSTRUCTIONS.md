# 🔧 CRITICAL FIX: Render Start Command Error

## ❌ Current Error

```
ModuleNotFoundError: No module named 'app'
==> Running 'gunicorn app:app'
```

**Problem:** Render is trying to run `gunicorn app:app` but your project is Django, not Flask!

---

## ✅ YOUR PROJECT STRUCTURE

```
backend/                    ← Root Directory
├── manage.py
├── requirements.txt
├── config/                 ← Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py            ← This is what gunicorn needs!
└── posts/
```

**Correct Start Command:** `gunicorn config.wsgi:application`

---

## 🛠️ FIX IN RENDER DASHBOARD (DO THIS NOW)

### Step 1: Go to Render Dashboard

1. Open https://dashboard.render.com/
2. Click on your web service (srushti-backend or similar)
3. Click **"Settings"** (left sidebar)

### Step 2: Fix Root Directory

Scroll to **"Root Directory"**

**Set to:** `backend`

✅ Exactly as written, no quotes, no slashes

### Step 3: Fix Start Command

Scroll to **"Start Command"**

**Current (WRONG):** `gunicorn app:app`

**Change to:** `gunicorn config.wsgi:application`

✅ Exactly as written
✅ No quotes
✅ No extra spaces

### Step 4: Save Changes

Click **"Save Changes"** button at the bottom

---

## 🚀 Step 5: Trigger Redeploy

After saving:

1. Scroll to top of page
2. Click **"Manual Deploy"** button
3. Select **"Deploy latest commit"**
4. Click **"Deploy"**

---

## 📊 What to Watch For

### ✅ SUCCESS Indicators (in logs):

```
✅ Installing dependencies...
✅ Collecting static files...
✅ Starting gunicorn 25.0.1
✅ Booting worker with pid: XXXX
✅ Listening at: http://0.0.0.0:10000
```

Then status changes to **"Live"** (green badge)

### ❌ FAILURE Indicators:

```
❌ ModuleNotFoundError: No module named 'app'
❌ Running 'gunicorn app:app'
```

If you still see this, the settings didn't save correctly. Try again.

---

## 🎯 After Deployment Succeeds

### 1. Run Migrations

In Render Dashboard → **Shell** tab:

```bash
python manage.py migrate
```

### 2. Create Superuser

```bash
python manage.py createsuperuser
```

### 3. Test Your API

Visit: `https://your-app.onrender.com/api/posts/`

**Expected:** DRF browsable API or JSON response

---

## 🔍 Why This Happened

**render.yaml had correct settings:**
```yaml
rootDir: backend
startCommand: "gunicorn config.wsgi:application"
```

**BUT:** Render Dashboard settings **override** render.yaml!

**Solution:** Update the Dashboard settings directly (which you're doing now)

---

## ✅ Verification Checklist

Before clicking "Deploy":

- [ ] Root Directory = `backend`
- [ ] Start Command = `gunicorn config.wsgi:application`
- [ ] Build Command = `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- [ ] Clicked "Save Changes"

After deployment:

- [ ] Logs show "Starting gunicorn"
- [ ] Logs show "Listening at: http://0.0.0.0:10000"
- [ ] Status shows "Live" (green)
- [ ] No "ModuleNotFoundError" in logs

---

## 🆘 If It Still Fails

1. **Double-check the Start Command** - Must be EXACTLY:
   ```
   gunicorn config.wsgi:application
   ```

2. **Check Root Directory** - Must be EXACTLY:
   ```
   backend
   ```

3. **Clear browser cache** - Sometimes Render UI doesn't update

4. **Delete and recreate service** - Last resort if settings won't save

---

## 📞 Quick Reference

**Your Configuration:**
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start Command: `gunicorn config.wsgi:application`

**Your Project Structure:**
- WSGI file location: `backend/config/wsgi.py`
- Django project name: `config`
- WSGI module path: `config.wsgi`
- WSGI application: `application`

---

**GO TO RENDER DASHBOARD NOW AND MAKE THESE CHANGES!**

After you save and redeploy, the deployment should succeed.
