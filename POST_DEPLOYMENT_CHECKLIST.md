# 📋 POST-DEPLOYMENT CHECKLIST

After deploying to Render, follow these steps to verify and test your deployment.

---

## ✅ STEP 1: Verify Deployment Status

### In Render Dashboard:

1. **Check Service Status**
   - [ ] Service shows green "Live" badge
   - [ ] No red errors in the Events tab
   - [ ] Latest deploy shows "Deploy succeeded"

2. **Check Logs**
   - [ ] Logs show: `Starting gunicorn 25.0.1`
   - [ ] Logs show: `Listening at: http://0.0.0.0:10000`
   - [ ] No Python errors or tracebacks
   - [ ] No "ModuleNotFoundError" errors

---

## ✅ STEP 2: Run Database Migrations

### In Render Shell (Dashboard → Shell tab):

```bash
python manage.py migrate
```

**Expected Output:**
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying posts.0001_initial... OK
  ...
```

**Checklist:**
- [ ] All migrations applied successfully
- [ ] No errors in migration output
- [ ] Database tables created

---

## ✅ STEP 3: Create Superuser (Optional but Recommended)

### In Render Shell:

```bash
python manage.py createsuperuser
```

**Follow prompts:**
- Username: (your choice)
- Email: (your email)
- Password: (strong password)

**Checklist:**
- [ ] Superuser created successfully
- [ ] Credentials saved securely

---

## ✅ STEP 4: Manual Testing

### Test 1: API Root Endpoint

**URL:** `https://your-app.onrender.com/api/posts/`

**Expected Result:**
- [ ] Page loads without errors
- [ ] Shows DRF browsable API interface OR JSON response
- [ ] Status code: 200 OK

**If you see errors:**
- Check Render logs for Python errors
- Verify DATABASE_URL is set
- Verify migrations were run

---

### Test 2: Admin Panel

**URL:** `https://your-app.onrender.com/admin/`

**Expected Result:**
- [ ] Django admin login page appears
- [ ] CSS/styling loads correctly (WhiteNoise working)
- [ ] Can login with superuser credentials
- [ ] Can see "Posts" in admin interface

**If styling is broken:**
- Check if collectstatic ran during build
- Verify WhiteNoise is in MIDDLEWARE
- Check Render logs for static file errors

---

### Test 3: Create a Post via API

**Using DRF Browsable API:**

1. Go to: `https://your-app.onrender.com/api/posts/`
2. Scroll to bottom of page
3. Fill in the form:
   - Title: "Test Post"
   - Content: "Testing deployment"
   - Platform: "twitter"
   - Status: "draft"
4. Click "POST"

**Expected Result:**
- [ ] Post created successfully
- [ ] Returns 201 Created status
- [ ] New post appears in the list

---

### Test 4: CRUD Operations

**Create:**
- [ ] Can create new posts via API
- [ ] Can create posts via admin panel

**Read:**
- [ ] Can view list of posts: `/api/posts/`
- [ ] Can view single post: `/api/posts/1/`
- [ ] Can view posts in admin panel

**Update:**
- [ ] Can update post via API (PUT/PATCH)
- [ ] Can update post via admin panel

**Delete:**
- [ ] Can delete post via API (DELETE)
- [ ] Can delete post via admin panel

---

## ✅ STEP 5: Automated Testing

### Run the Test Script:

1. **Update the script with your Render URL:**
   ```python
   # In test_render_deployment.py
   RENDER_URL = "https://your-actual-app.onrender.com"
   ```

2. **Install requests library (if not already):**
   ```bash
   pip install requests
   ```

3. **Run the test:**
   ```bash
   python test_render_deployment.py
   ```

**Expected Output:**
```
============================================================
RENDER DEPLOYMENT VERIFICATION
============================================================

Testing API Health...
✓ API is accessible
  → Status: 200

Testing GET /api/posts/...
✓ GET posts endpoint
  → Found X posts

Testing POST /api/posts/...
✓ POST create post
  → Created post ID: X

Testing GET /api/posts/X/...
✓ GET single post
  → Title: Test Post

Testing PUT /api/posts/X/...
✓ PUT update post
  → Status: published

Testing DELETE /api/posts/X/...
✓ DELETE post
  → Post deleted successfully

Testing Admin Panel...
✓ Admin panel accessible
  → Login page loads

Testing Static Files...
✓ Static files served
  → WhiteNoise is working

============================================================
TEST SUMMARY
============================================================
Passed: 8
Failed: 0

🎉 All tests passed! Your deployment is successful!
```

**Checklist:**
- [ ] All 8 tests pass
- [ ] No failed tests
- [ ] Script completes without errors

---

## ✅ STEP 6: Performance Check

### Check Response Times:

**Using browser DevTools:**
1. Open DevTools (F12)
2. Go to Network tab
3. Visit: `https://your-app.onrender.com/api/posts/`
4. Check response time

**Expected:**
- [ ] First request: < 5 seconds (cold start on free tier)
- [ ] Subsequent requests: < 1 second
- [ ] No timeout errors

**Note:** Render free tier has cold starts (app sleeps after inactivity)

---

## ✅ STEP 7: Environment Variables Verification

### In Render Dashboard → Environment:

**Verify these are set:**
- [ ] `SECRET_KEY` - Set to a long random string
- [ ] `DEBUG` - Set to exactly: `False` (no quotes)
- [ ] `DATABASE_URL` - Auto-set by PostgreSQL database

**Security Check:**
- [ ] SECRET_KEY is NOT the default Django key
- [ ] DEBUG is False (not True)
- [ ] No sensitive data in environment variables

---

## ✅ STEP 8: Database Verification

### In Render Shell:

```bash
python manage.py dbshell
```

Then run:
```sql
\dt  -- List all tables
SELECT COUNT(*) FROM posts_post;  -- Count posts
\q   -- Quit
```

**Checklist:**
- [ ] Database connection works
- [ ] Tables exist (posts_post, auth_user, etc.)
- [ ] Can query data

---

## ✅ STEP 9: Logs Monitoring

### Check for Common Issues:

**In Render Logs tab, look for:**

**Good Signs (✅):**
- `Starting gunicorn`
- `Listening at: http://0.0.0.0:10000`
- `GET /api/posts/ HTTP/1.1" 200`
- No error tracebacks

**Bad Signs (❌):**
- `ModuleNotFoundError`
- `ImproperlyConfigured`
- `OperationalError` (database issues)
- `500 Internal Server Error`
- Python tracebacks

**Checklist:**
- [ ] No errors in recent logs
- [ ] Successful request logs visible
- [ ] No database connection errors

---

## ✅ STEP 10: Final Verification

### Complete Checklist:

**Deployment:**
- [ ] Service is "Live" (green badge)
- [ ] Latest deploy succeeded
- [ ] No errors in Render logs

**Database:**
- [ ] Migrations completed
- [ ] Database connection working
- [ ] Can create/read/update/delete data

**API:**
- [ ] `/api/posts/` returns 200
- [ ] Can perform all CRUD operations
- [ ] JSON responses are correct

**Admin:**
- [ ] Admin panel accessible
- [ ] Static files load correctly
- [ ] Can login and manage posts

**Testing:**
- [ ] Automated tests pass
- [ ] Manual testing successful
- [ ] No errors in browser console

**Security:**
- [ ] DEBUG = False
- [ ] SECRET_KEY is secure
- [ ] .env not in repository

---

## 🎉 SUCCESS CRITERIA

Your deployment is fully successful when:

1. ✅ All items in this checklist are checked
2. ✅ Automated test script passes all tests
3. ✅ Can create, read, update, and delete posts
4. ✅ Admin panel works correctly
5. ✅ No errors in Render logs
6. ✅ API responds within acceptable time

---

## 🆘 TROUBLESHOOTING

### If Tests Fail:

1. **Check Render Logs First**
   - Look for Python errors
   - Check for missing dependencies
   - Verify database connection

2. **Verify Environment Variables**
   - Ensure all required variables are set
   - Check for typos in variable names
   - Verify DEBUG = False (not "False")

3. **Re-run Migrations**
   ```bash
   python manage.py migrate --run-syncdb
   ```

4. **Check Database Connection**
   ```bash
   python manage.py dbshell
   ```

5. **Restart Service**
   - In Render dashboard: Manual Deploy → Deploy latest commit

---

## 📊 MONITORING AFTER DEPLOYMENT

### Daily Checks:

- [ ] Check Render dashboard for service status
- [ ] Review logs for any errors
- [ ] Test API endpoints periodically

### Weekly Checks:

- [ ] Review database size (free tier has limits)
- [ ] Check for any security updates
- [ ] Verify backups (if configured)

---

## 📞 NEED HELP?

If you encounter issues:

1. **Check Render Logs** - Most issues show up here
2. **Review RENDER_DEPLOYMENT_VALIDATION.md** - Troubleshooting section
3. **Verify Configuration** - Compare with QUICK_DEPLOY_GUIDE.md
4. **Test Locally** - Ensure it works locally first

---

**Deployment Date:** _________________

**Deployed By:** _________________

**Render URL:** _________________

**Notes:** _________________
