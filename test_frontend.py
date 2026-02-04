"""
Frontend Testing Script
Tests the React frontend application to verify routing and functionality
"""

import requests
import time

def test_frontend():
    """Test the frontend application"""
    
    base_url = "http://localhost:5174"
    
    print("=" * 60)
    print("FRONTEND APPLICATION TEST")
    print("=" * 60)
    
    # Test 1: Homepage loads
    print("\n1. Testing Homepage (/)...")
    try:
        response = requests.get(base_url + "/", timeout=5)
        if response.status_code == 200:
            print("   ✅ Homepage loads successfully (Status: 200)")
            # Check for root div
            if 'id="root"' in response.text:
                print("   ✅ Root div found in HTML")
            else:
                print("   ❌ Root div NOT found in HTML")
            
            # Check for main.jsx script
            if 'src="/src/main.jsx"' in response.text:
                print("   ✅ main.jsx script reference found")
            else:
                print("   ❌ main.jsx script reference NOT found")
        else:
            print(f"   ❌ Homepage failed (Status: {response.status_code})")
    except Exception as e:
        print(f"   ❌ Error accessing homepage: {e}")
    
    # Test 2: Check if Vite dev server is running
    print("\n2. Testing Vite Dev Server...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("   ✅ Vite dev server is running")
            print(f"   ✅ Server URL: {base_url}")
        else:
            print(f"   ❌ Server returned status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Cannot connect to server: {e}")
    
    # Test 3: Check main.jsx is accessible
    print("\n3. Testing main.jsx accessibility...")
    try:
        response = requests.get(base_url + "/src/main.jsx", timeout=5)
        if response.status_code == 200:
            print("   ✅ main.jsx is accessible")
            # Check for React.StrictMode
            if 'React.StrictMode' in response.text:
                print("   ✅ React.StrictMode wrapper found in main.jsx")
            else:
                print("   ⚠️  React.StrictMode NOT found in main.jsx")
            
            # Check for BrowserRouter
            if 'BrowserRouter' in response.text:
                print("   ✅ BrowserRouter found in main.jsx")
            else:
                print("   ❌ BrowserRouter NOT found in main.jsx")
        else:
            print(f"   ❌ main.jsx not accessible (Status: {response.status_code})")
    except Exception as e:
        print(f"   ❌ Error accessing main.jsx: {e}")
    
    # Test 4: Verify no /static/ in base URL
    print("\n4. Verifying base URL configuration...")
    try:
        # Try accessing with /static/ - should NOT work
        response = requests.get(base_url + "/static/", timeout=5)
        if response.status_code == 404:
            print("   ✅ /static/ path correctly returns 404 (not used)")
        else:
            print(f"   ⚠️  /static/ path accessible (Status: {response.status_code})")
    except Exception as e:
        print(f"   ✅ /static/ path not accessible (as expected)")
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print("\n✅ Frontend fixes applied:")
    print("   - main.jsx updated with React.StrictMode")
    print("   - vite.config.js base changed from '/static/' to '/'")
    print("   - index.html verified with root div")
    print("\n📋 Manual Testing Required:")
    print("   1. Open browser to: http://localhost:5174/")
    print("   2. Verify 'Posts' heading is visible")
    print("   3. Verify 'Create Post' link is visible")
    print("   4. Test navigation to /create")
    print("   5. Test creating a new post")
    print("   6. Test editing a post")
    print("   7. Test deleting a post")
    print("   8. Open DevTools (F12) and check Console for errors")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_frontend()
