# 🖥️ RENDER SHELL COMMANDS - QUICK REFERENCE

**Quick copy-paste commands for Render Shell**

---

## 📍 HOW TO ACCESS RENDER SHELL

1. Go to: https://dashboard.render.com
2. Click on your service (e.g., "srushti-backend")
3. Click the **"Shell"** tab in the top navigation
4. Wait for shell to load (you'll see a `$` prompt)

---

## ✅ ESSENTIAL POST-DEPLOYMENT COMMANDS

### 1. Run Database Migrations

```bash
python manage.py migrate
```

**Expected:** All migrations show "OK"

---

### 2. Create Superuser

```bash
python manage.py createsuperuser
```

**Follow prompts:**
- Username: (your choice)
- Email: (your email)
- Password: (strong password)

---

### 3. Verify Database Connection

```bash
python manage.py dbshell
```

**Then run:**
```sql
\dt
\q
```

---

### 4. Check Installed Apps

```bash
python manage.py showmigrations
```

**Shows:** All apps and their migration status

---

### 5. Collect Static Files (if needed)

```bash
python manage.py collectstatic --noinput
```

**Use if:** Static files aren't loading

---

## 🔍 DIAGNOSTIC COMMANDS

### Check Django Version

```bash
python -c "import django; print(django.get_version())"
```

---

### Check Database Tables

```bash
python manage.py dbshell
```

```sql
\dt
SELECT COUNT(*) FROM content_posts_socialpost;
\q
```

---

### List All Users

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
print(User.objects.all())
exit()
```

---

### Check Environment Variables

```bash
echo $DATABASE_URL
echo $DEBUG
echo $SECRET_KEY
```

---

### Test Database Connection

```bash
python manage.py check --database default
```

---

## 🛠️ TROUBLESHOOTING COMMANDS

### Re-run Migrations with Sync

```bash
python manage.py migrate --run-syncdb
```

**Use if:** Regular migrate fails

---

### Create Missing Tables

```bash
python manage.py migrate --fake-initial
```

**Use if:** Tables already exist but migrations aren't marked as applied

---

### Clear Sessions

```bash
python manage.py clearsessions
```

---

### Flush Database (⚠️ DANGER - Deletes all data!)

```bash
python manage.py flush
```

**WARNING:** This deletes ALL data! Only use for testing.

---

## 📊 DATA MANAGEMENT COMMANDS

### Create Test Data

```bash
python manage.py shell
```

```python
from content_posts.models import SocialPost

# Create a test post
post = SocialPost.objects.create(
    title="Test Post",
    content="This is a test post",
    platform="twitter",
    status="draft"
)
print(f"Created post: {post.id}")
exit()
```

---

### Count Posts

```bash
python manage.py shell
```

```python
from content_posts.models import SocialPost
print(f"Total posts: {SocialPost.objects.count()}")
exit()
```

---

### List All Posts

```bash
python manage.py shell
```

```python
from content_posts.models import SocialPost
for post in SocialPost.objects.all():
    print(f"{post.id}: {post.title} - {post.status}")
exit()
```

---

## 🔐 USER MANAGEMENT COMMANDS

### List All Superusers

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f"{user.username} - {user.email}")
exit()
```

---

### Change User Password

```bash
python manage.py changepassword <username>
```

---

### Create Superuser (Non-Interactive)

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'your-password')
exit()
```

---

## 📝 MIGRATION COMMANDS

### Show Migration Status

```bash
python manage.py showmigrations
```

---

### Create New Migrations

```bash
python manage.py makemigrations
```

---

### Show SQL for Migration

```bash
python manage.py sqlmigrate content_posts 0001
```

---

### Migrate Specific App

```bash
python manage.py migrate content_posts
```

---

## 🧪 TESTING COMMANDS

### Run All Tests

```bash
python manage.py test
```

---

### Run Specific App Tests

```bash
python manage.py test content_posts
```

---

### Run with Verbose Output

```bash
python manage.py test --verbosity=2
```

---

## 🔧 UTILITY COMMANDS

### Django Shell

```bash
python manage.py shell
```

**Interactive Python shell with Django loaded**

---

### Check Project Configuration

```bash
python manage.py check
```

---

### Show URLs

```bash
python manage.py show_urls
```

**Note:** Requires django-extensions

---

### Generate Secret Key

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 📦 PACKAGE MANAGEMENT

### List Installed Packages

```bash
pip list
```

---

### Check Package Version

```bash
pip show django
```

---

### Install Missing Package

```bash
pip install package-name
```

**Note:** Changes won't persist after restart. Add to requirements.txt instead.

---

## 🚨 EMERGENCY COMMANDS

### Reset Database (⚠️ DANGER!)

```bash
python manage.py flush --noinput
python manage.py migrate
python manage.py createsuperuser
```

---

### Clear All Sessions

```bash
python manage.py clearsessions
```

---

### Rebuild Static Files

```bash
python manage.py collectstatic --noinput --clear
```

---

## 📋 COMMON COMMAND SEQUENCES

### Initial Setup (After First Deploy)

```bash
# 1. Run migrations
python manage.py migrate

# 2. Create superuser
python manage.py createsuperuser

# 3. Verify
python manage.py check
```

---

### After Code Changes

```bash
# 1. Run new migrations
python manage.py migrate

# 2. Collect static files
python manage.py collectstatic --noinput

# 3. Check for issues
python manage.py check
```

---

### Troubleshooting Sequence

```bash
# 1. Check configuration
python manage.py check

# 2. Verify database
python manage.py dbshell
\dt
\q

# 3. Check migrations
python manage.py showmigrations

# 4. Re-run migrations
python manage.py migrate --run-syncdb
```

---

## 💡 TIPS

1. **Copy-Paste Carefully:** Render Shell can be finicky with pasting
2. **Wait for Prompts:** Some commands take time to respond
3. **Check Output:** Always verify command succeeded
4. **Exit Shell Properly:** Use `exit()` for Python shell, `\q` for DB shell
5. **Session Timeout:** Shell sessions timeout after inactivity

---

## 🔗 QUICK LINKS

- **Render Dashboard:** https://dashboard.render.com
- **Your Service:** https://dashboard.render.com/web/[your-service-id]
- **Shell Tab:** Click "Shell" in top navigation
- **Logs Tab:** Click "Logs" to see output

---

## 📞 NEED HELP?

If commands fail:
1. Check Render Logs tab for errors
2. Verify environment variables are set
3. Ensure DATABASE_URL is connected
4. Review RENDER_POST_DEPLOYMENT_GUIDE.md
5. Check POST_DEPLOYMENT_CHECKLIST.md

---

**Last Updated:** 2024
**For:** Django on Render Platform
