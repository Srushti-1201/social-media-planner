"""
Post-Deployment Testing Script for Render
Run this after deploying to Render to verify everything works
"""

import requests
import sys
from datetime import datetime

# CONFIGURATION - Replace with your actual Render URL
RENDER_URL = "https://your-app.onrender.com"  # Replace with your actual URL
API_BASE = f"{RENDER_URL}/api"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_test(name, status, message=""):
    """Print test result with color"""
    if status:
        print(f"{Colors.GREEN}✓{Colors.END} {name}")
        if message:
            print(f"  {Colors.BLUE}→{Colors.END} {message}")
    else:
        print(f"{Colors.RED}✗{Colors.END} {name}")
        if message:
            print(f"  {Colors.RED}→{Colors.END} {message}")

def test_api_health():
    """Test if API is accessible"""
    print(f"\n{Colors.YELLOW}Testing API Health...{Colors.END}")
    
    try:
        response = requests.get(f"{API_BASE}/posts/", timeout=10)
        if response.status_code == 200:
            print_test("API is accessible", True, f"Status: {response.status_code}")
            return True
        else:
            print_test("API is accessible", False, f"Status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print_test("API is accessible", False, f"Error: {str(e)}")
        return False

def test_get_posts():
    """Test GET /api/posts/"""
    print(f"\n{Colors.YELLOW}Testing GET /api/posts/...{Colors.END}")
    
    try:
        response = requests.get(f"{API_BASE}/posts/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print_test("GET posts endpoint", True, f"Found {len(data)} posts")
            return True
        else:
            print_test("GET posts endpoint", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("GET posts endpoint", False, f"Error: {str(e)}")
        return False

def test_create_post():
    """Test POST /api/posts/"""
    print(f"\n{Colors.YELLOW}Testing POST /api/posts/...{Colors.END}")
    
    test_post = {
        "title": f"Test Post - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": "This is a test post created by the deployment verification script.",
        "platform": "twitter",
        "status": "draft"
    }
    
    try:
        response = requests.post(
            f"{API_BASE}/posts/",
            json=test_post,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 201:
            data = response.json()
            post_id = data.get('id')
            print_test("POST create post", True, f"Created post ID: {post_id}")
            return post_id
        else:
            print_test("POST create post", False, f"Status: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print_test("POST create post", False, f"Error: {str(e)}")
        return None

def test_get_single_post(post_id):
    """Test GET /api/posts/{id}/"""
    print(f"\n{Colors.YELLOW}Testing GET /api/posts/{post_id}/...{Colors.END}")
    
    try:
        response = requests.get(f"{API_BASE}/posts/{post_id}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print_test("GET single post", True, f"Title: {data.get('title')}")
            return True
        else:
            print_test("GET single post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("GET single post", False, f"Error: {str(e)}")
        return False

def test_update_post(post_id):
    """Test PUT /api/posts/{id}/"""
    print(f"\n{Colors.YELLOW}Testing PUT /api/posts/{post_id}/...{Colors.END}")
    
    updated_data = {
        "title": f"Updated Test Post - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": "This post has been updated by the deployment verification script.",
        "platform": "twitter",
        "status": "published"
    }
    
    try:
        response = requests.put(
            f"{API_BASE}/posts/{post_id}/",
            json=updated_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            print_test("PUT update post", True, f"Status: {data.get('status')}")
            return True
        else:
            print_test("PUT update post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("PUT update post", False, f"Error: {str(e)}")
        return False

def test_delete_post(post_id):
    """Test DELETE /api/posts/{id}/"""
    print(f"\n{Colors.YELLOW}Testing DELETE /api/posts/{post_id}/...{Colors.END}")
    
    try:
        response = requests.delete(f"{API_BASE}/posts/{post_id}/", timeout=10)
        if response.status_code == 204:
            print_test("DELETE post", True, "Post deleted successfully")
            return True
        else:
            print_test("DELETE post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("DELETE post", False, f"Error: {str(e)}")
        return False

def test_admin_panel():
    """Test if admin panel is accessible"""
    print(f"\n{Colors.YELLOW}Testing Admin Panel...{Colors.END}")
    
    try:
        response = requests.get(f"{RENDER_URL}/admin/", timeout=10)
        if response.status_code == 200:
            print_test("Admin panel accessible", True, "Login page loads")
            return True
        else:
            print_test("Admin panel accessible", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("Admin panel accessible", False, f"Error: {str(e)}")
        return False

def test_static_files():
    """Test if static files are being served"""
    print(f"\n{Colors.YELLOW}Testing Static Files...{Colors.END}")
    
    try:
        # Test admin CSS (should be served by WhiteNoise)
        response = requests.get(f"{RENDER_URL}/static/admin/css/base.css", timeout=10)
        if response.status_code == 200:
            print_test("Static files served", True, "WhiteNoise is working")
            return True
        else:
            print_test("Static files served", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("Static files served", False, f"Error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}RENDER DEPLOYMENT VERIFICATION{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"\nTesting URL: {Colors.YELLOW}{RENDER_URL}{Colors.END}")
    
    if RENDER_URL == "https://your-app.onrender.com":
        print(f"\n{Colors.RED}ERROR: Please update RENDER_URL in this script with your actual Render URL{Colors.END}")
        sys.exit(1)
    
    results = {
        "passed": 0,
        "failed": 0
    }
    
    # Test 1: API Health
    if test_api_health():
        results["passed"] += 1
    else:
        results["failed"] += 1
        print(f"\n{Colors.RED}API is not accessible. Check Render logs and ensure deployment succeeded.{Colors.END}")
        sys.exit(1)
    
    # Test 2: GET posts
    if test_get_posts():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Test 3: CREATE post
    post_id = test_create_post()
    if post_id:
        results["passed"] += 1
        
        # Test 4: GET single post
        if test_get_single_post(post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
        
        # Test 5: UPDATE post
        if test_update_post(post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
        
        # Test 6: DELETE post
        if test_delete_post(post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
    else:
        results["failed"] += 4  # All CRUD tests failed
    
    # Test 7: Admin panel
    if test_admin_panel():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Test 8: Static files
    if test_static_files():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Summary
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}TEST SUMMARY{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.GREEN}Passed: {results['passed']}{Colors.END}")
    print(f"{Colors.RED}Failed: {results['failed']}{Colors.END}")
    
    if results['failed'] == 0:
        print(f"\n{Colors.GREEN}🎉 All tests passed! Your deployment is successful!{Colors.END}")
        return 0
    else:
        print(f"\n{Colors.YELLOW}⚠️  Some tests failed. Check the errors above.{Colors.END}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
