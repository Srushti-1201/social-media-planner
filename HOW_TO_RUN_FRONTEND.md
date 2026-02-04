# How to Execute and View the Frontend Application

## 🚀 Quick Start (Frontend is Already Running!)

Good news! The frontend dev server is **already running** on your system.

### Step 1: Open Your Browser

The frontend is currently accessible at:

```
http://localhost:5174/
```

**To open it:**

**Option A - Click the link** (if your terminal supports it):
- Look for the terminal output that says: `➜  Local:   http://localhost:5174/`
- Click on the link

**Option B - Manual browser open**:
1. Open any web browser (Chrome, Firefox, Edge, etc.)
2. Type in the address bar: `http://localhost:5174/`
3. Press Enter

**Option C - Use Windows command** (already executed):
```bash
start http://localhost:5174/
```

---

## 📋 What You Should See

Once you open `http://localhost:5174/` in your browser, you should see:

1. **Page Title**: "Posts" or similar heading
2. **Navigation**: "Create Post" link/button
3. **Content**: List of posts (or empty state if no posts exist)
4. **Working Routes**:
   - `/` - Homepage with post list
   - `/create` - Create new post form
   - `/edit/:id` - Edit existing post form

---

## 🔧 If the Server is NOT Running

If for some reason the server stopped, here's how to start it:

### Method 1: Using VSCode Terminal

1. **Open a new terminal in VSCode**:
   - Press `` Ctrl + ` `` (backtick) or
   - Menu: Terminal → New Terminal

2. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

3. **Start the dev server**:
   ```bash
   npm run dev
   ```

4. **Wait for output**:
   ```
   VITE v7.3.1  ready in XXX ms
   
   ➜  Local:   http://localhost:5173/
   ➜  Network: use --host to expose
   ```

5. **Open the URL shown** (usually http://localhost:5173/ or http://localhost:5174/)

### Method 2: Using Windows Command Prompt

1. **Open Command Prompt**:
   - Press `Win + R`
   - Type `cmd`
   - Press Enter

2. **Navigate to your project**:
   ```bash
   cd C:\Users\prabu\Downloads\SRUSHTI\frontend
   ```

3. **Start the server**:
   ```bash
   npm run dev
   ```

4. **Open the URL in browser**

---

## 🧪 Testing the Application

### 1. Homepage Test
- URL: `http://localhost:5174/`
- Should show: Posts list

### 2. Create Post Test
- Click "Create Post" link
- URL should change to: `http://localhost:5174/create`
- Should show: Form to create a new post
- Fill in the form and submit

### 3. Edit Post Test
- Click "Edit" button on any post
- URL should change to: `http://localhost:5174/edit/[post-id]`
- Should show: Form with existing post data
- Modify and save

### 4. Delete Post Test
- Click "Delete" button on any post
- Post should be removed from the list

---

## 🐛 Troubleshooting

### Problem: "This site can't be reached"

**Solution**:
1. Check if the dev server is running (look for terminal with Vite output)
2. If not running, start it using the commands above
3. Make sure you're using the correct port (5173 or 5174)

### Problem: Blank/White Page

**Solution**:
1. Open Browser DevTools:
   - Press `F12` or
   - Right-click → Inspect
2. Go to "Console" tab
3. Look for any red error messages
4. Share the errors if you need help

### Problem: "Cannot GET /"

**Solution**:
1. This means the server isn't running
2. Follow the "If the Server is NOT Running" section above

### Problem: Port Already in Use

**Solution**:
Vite will automatically use the next available port:
- If 5173 is busy → uses 5174
- If 5174 is busy → uses 5175
- etc.

Just use the port shown in the terminal output.

---

## 📱 Viewing on Mobile/Other Devices

To view on other devices on the same network:

1. **Find your computer's IP address**:
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. **Start server with host flag**:
   ```bash
   npm run dev -- --host
   ```

3. **Access from other device**:
   ```
   http://[YOUR-IP]:5174/
   ```
   Example: `http://192.168.1.100:5174/`

---

## 🛑 Stopping the Server

To stop the frontend dev server:

1. Go to the terminal where it's running
2. Press `Ctrl + C`
3. Confirm if prompted

---

## ✅ Current Status

**Server Status**: ✅ RUNNING
**Port**: 5174
**URL**: http://localhost:5174/
**Browser**: Should already be open

**Just open your browser and navigate to http://localhost:5174/ to see your application!**

---

## 🎯 Quick Commands Reference

```bash
# Navigate to frontend
cd frontend

# Install dependencies (if needed)
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## 📞 Need Help?

If you encounter any issues:
1. Check the terminal for error messages
2. Check browser console (F12) for errors
3. Verify all files are saved
4. Try restarting the dev server
5. Clear browser cache and reload (Ctrl + Shift + R)
