"""
Enhanced Post-Deployment Testing Script for Render
Automatically prompts for Render URL and runs comprehensive tests
"""

import requests
import sys
from datetime import datetime
import os

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Print a header with formatting"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{text.center(70)}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'='*70}{Colors.END}\n")

def print_section(text):
    """Print a section header"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'─'*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'─'*70}{Colors.END}")

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

def print_info(message):
    """Print info message"""
    print(f"{Colors.YELLOW}ℹ{Colors.END} {message}")

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✓{Colors.END} {message}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}✗{Colors.END} {message}")

def get_render_url():
    """Prompt user for Render URL"""
    print_section("CONFIGURATION")
    print_info("Please enter your Render app URL")
    print(f"{Colors.YELLOW}Examples:{Colors.END}")
    print("  • https://my-app.onrender.com")
    print("  • https://srushti-backend.onrender.com")
    print()
    
    while True:
        url = input(f"{Colors.CYAN}Enter your Render URL: {Colors.END}").strip()
        
        # Remove trailing slash if present
        url = url.rstrip('/')
        
        # Validate URL format
        if not url:
            print_error("URL cannot be empty. Please try again.")
            continue
        
        if not url.startswith('http'):
            print_error("URL must start with http:// or https://")
            continue
        
        if 'onrender.com' not in url:
            print_error("This doesn't look like a Render URL. Continue anyway? (y/n)")
            confirm = input().strip().lower()
            if confirm != 'y':
                continue
        
        # Confirm with user
        print(f"\n{Colors.YELLOW}You entered:{Colors.END} {Colors.BOLD}{url}{Colors.END}")
        confirm = input(f"{Colors.CYAN}Is this correct? (y/n): {Colors.END}").strip().lower()
        
        if confirm == 'y':
            return url
        else:
            print_info("Let's try again...")

def test_api_health(api_base):
    """Test if API is accessible"""
    print_section("TEST 1: API HEALTH CHECK")
    
    try:
        print_info(f"Testing: {api_base}/posts/")
        response = requests.get(f"{api_base}/posts/", timeout=15)
        
        if response.status_code == 200:
            print_test("API is accessible", True, f"Status: {response.status_code}")
            return True
        else:
            print_test("API is accessible", False, f"Status: {response.status_code}")
            print_error(f"Response: {response.text[:200]}")
            return False
    except requests.exceptions.Timeout:
        print_test("API is accessible", False, "Request timed out (>15s)")
        print_info("Note: Render free tier may have cold starts. Try again in a moment.")
        return False
    except requests.exceptions.RequestException as e:
        print_test("API is accessible", False, f"Error: {str(e)}")
        return False

def test_get_posts(api_base):
    """Test GET /api/posts/"""
    print_section("TEST 2: GET ALL POSTS")
    
    try:
        response = requests.get(f"{api_base}/posts/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            count = len(data) if isinstance(data, list) else 'unknown'
            print_test("GET posts endpoint", True, f"Found {count} posts")
            
            if isinstance(data, list) and len(data) > 0:
                print_info(f"Sample post: {data[0].get('title', 'N/A')}")
            
            return True
        else:
            print_test("GET posts endpoint", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("GET posts endpoint", False, f"Error: {str(e)}")
        return False

def test_create_post(api_base):
    """Test POST /api/posts/"""
    print_section("TEST 3: CREATE POST")
    
    test_post = {
        "title": f"Automated Test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": "This post was created by the automated deployment verification script.",
        "platform": "twitter",
        "status": "draft"
    }
    
    try:
        print_info(f"Creating test post: '{test_post['title']}'")
        response = requests.post(
            f"{api_base}/posts/",
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
            print_test("POST create post", False, f"Status: {response.status_code}")
            print_error(f"Response: {response.text[:200]}")
            return None
    except Exception as e:
        print_test("POST create post", False, f"Error: {str(e)}")
        return None

def test_get_single_post(api_base, post_id):
    """Test GET /api/posts/{id}/"""
    print_section("TEST 4: GET SINGLE POST")
    
    try:
        print_info(f"Fetching post ID: {post_id}")
        response = requests.get(f"{api_base}/posts/{post_id}/", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            title = data.get('title', 'N/A')
            print_test("GET single post", True, f"Title: {title}")
            return True
        else:
            print_test("GET single post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("GET single post", False, f"Error: {str(e)}")
        return False

def test_update_post(api_base, post_id):
    """Test PUT /api/posts/{id}/"""
    print_section("TEST 5: UPDATE POST")
    
    updated_data = {
        "title": f"Updated Test - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "content": "This post has been updated by the automated verification script.",
        "platform": "twitter",
        "status": "published"
    }
    
    try:
        print_info(f"Updating post ID: {post_id}")
        response = requests.put(
            f"{api_base}/posts/{post_id}/",
            json=updated_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            status = data.get('status', 'N/A')
            print_test("PUT update post", True, f"New status: {status}")
            return True
        else:
            print_test("PUT update post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("PUT update post", False, f"Error: {str(e)}")
        return False

def test_delete_post(api_base, post_id):
    """Test DELETE /api/posts/{id}/"""
    print_section("TEST 6: DELETE POST")
    
    try:
        print_info(f"Deleting post ID: {post_id}")
        response = requests.delete(f"{api_base}/posts/{post_id}/", timeout=10)
        
        if response.status_code == 204:
            print_test("DELETE post", True, "Post deleted successfully")
            return True
        else:
            print_test("DELETE post", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("DELETE post", False, f"Error: {str(e)}")
        return False

def test_admin_panel(render_url):
    """Test if admin panel is accessible"""
    print_section("TEST 7: ADMIN PANEL")
    
    try:
        print_info(f"Testing: {render_url}/admin/")
        response = requests.get(f"{render_url}/admin/", timeout=10)
        
        if response.status_code == 200:
            # Check if it's actually the admin page
            if 'django' in response.text.lower() or 'admin' in response.text.lower():
                print_test("Admin panel accessible", True, "Login page loads correctly")
                return True
            else:
                print_test("Admin panel accessible", False, "Page loads but doesn't look like admin")
                return False
        else:
            print_test("Admin panel accessible", False, f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_test("Admin panel accessible", False, f"Error: {str(e)}")
        return False

def test_static_files(render_url):
    """Test if static files are being served"""
    print_section("TEST 8: STATIC FILES (WHITENOISE)")
    
    try:
        print_info(f"Testing: {render_url}/static/admin/css/base.css")
        response = requests.get(f"{render_url}/static/admin/css/base.css", timeout=10)
        
        if response.status_code == 200:
            print_test("Static files served", True, "WhiteNoise is working correctly")
            return True
        else:
            print_test("Static files served", False, f"Status: {response.status_code}")
            print_info("Static files may not be collected. Run: python manage.py collectstatic")
            return False
    except Exception as e:
        print_test("Static files served", False, f"Error: {str(e)}")
        return False

def print_summary(results):
    """Print test summary"""
    print_header("TEST SUMMARY")
    
    total = results['passed'] + results['failed']
    percentage = (results['passed'] / total * 100) if total > 0 else 0
    
    print(f"{Colors.GREEN}{Colors.BOLD}Passed: {results['passed']}/{total}{Colors.END}")
    print(f"{Colors.RED}{Colors.BOLD}Failed: {results['failed']}/{total}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}Success Rate: {percentage:.1f}%{Colors.END}")
    
    if results['failed'] == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 ALL TESTS PASSED!{Colors.END}")
        print(f"{Colors.GREEN}Your Render deployment is fully functional!{Colors.END}")
    elif results['passed'] >= 6:
        print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  MOSTLY SUCCESSFUL{Colors.END}")
        print(f"{Colors.YELLOW}Core functionality works, but some tests failed.{Colors.END}")
        print(f"{Colors.YELLOW}Review the errors above and check Render logs.{Colors.END}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ DEPLOYMENT ISSUES DETECTED{Colors.END}")
        print(f"{Colors.RED}Multiple tests failed. Please check:{Colors.END}")
        print(f"  1. Render service is running (green 'Live' badge)")
        print(f"  2. Migrations were run: python manage.py migrate")
        print(f"  3. Environment variables are set correctly")
        print(f"  4. Check Render logs for errors")

def print_next_steps(results):
    """Print recommended next steps"""
    print_header("NEXT STEPS")
    
    if results['failed'] == 0:
        print(f"{Colors.GREEN}✓{Colors.END} All tests passed! You can now:")
        print(f"  1. Create a superuser (if not done): python manage.py createsuperuser")
        print(f"  2. Login to admin panel and test manually")
        print(f"  3. Share your app URL with stakeholders")
        print(f"  4. Monitor Render logs for any issues")
    else:
        print(f"{Colors.YELLOW}⚠{Colors.END} Some tests failed. Recommended actions:")
        print(f"  1. Check Render dashboard → Logs tab")
        print(f"  2. Verify environment variables are set")
        print(f"  3. Run migrations in Render Shell: python manage.py migrate")
        print(f"  4. Check DATABASE_URL is connected")
        print(f"  5. Review POST_DEPLOYMENT_CHECKLIST.md")

def main():
    """Run all tests"""
    print_header("RENDER DEPLOYMENT VERIFICATION")
    print(f"{Colors.CYAN}Automated Post-Deployment Testing Script{Colors.END}")
    print(f"{Colors.CYAN}Version 2.0 - Enhanced Edition{Colors.END}")
    
    # Get Render URL from user
    render_url = get_render_url()
    api_base = f"{render_url}/api"
    
    print_header("STARTING TESTS")
    print_info(f"Testing URL: {Colors.BOLD}{render_url}{Colors.END}")
    print_info(f"API Base: {Colors.BOLD}{api_base}{Colors.END}")
    print_info("This will take approximately 30-60 seconds...")
    
    results = {
        "passed": 0,
        "failed": 0
    }
    
    # Test 1: API Health
    if test_api_health(api_base):
        results["passed"] += 1
    else:
        results["failed"] += 1
        print_error("\nAPI is not accessible. Stopping tests.")
        print_info("Please check:")
        print("  • Render service is running (green 'Live' badge)")
        print("  • Deployment succeeded (no errors in Events tab)")
        print("  • URL is correct")
        print_summary(results)
        return 1
    
    # Test 2: GET posts
    if test_get_posts(api_base):
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Test 3: CREATE post
    post_id = test_create_post(api_base)
    if post_id:
        results["passed"] += 1
        
        # Test 4: GET single post
        if test_get_single_post(api_base, post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
        
        # Test 5: UPDATE post
        if test_update_post(api_base, post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
        
        # Test 6: DELETE post
        if test_delete_post(api_base, post_id):
            results["passed"] += 1
        else:
            results["failed"] += 1
    else:
        results["failed"] += 4  # All CRUD tests failed
        print_error("Skipping remaining CRUD tests due to POST failure")
    
    # Test 7: Admin panel
    if test_admin_panel(render_url):
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Test 8: Static files
    if test_static_files(render_url):
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Print summary and next steps
    print_summary(results)
    print_next_steps(results)
    
    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}\n")
    
    return 0 if results['failed'] == 0 else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Test interrupted by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error: {str(e)}{Colors.END}")
        sys.exit(1)
