import requests
import sys
import json
from datetime import datetime

class StatusAPITester:
    def __init__(self, base_url="https://96459c88-a9e1-4eeb-85ef-df28c66cbd18.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.base_url}{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    print(f"Response: {json.dumps(response_data, indent=2)}")
                    return success, response_data
                except:
                    print(f"Response: {response.text}")
                    return success, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"Response: {response.text}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_health_check(self):
        """Test the health check endpoint"""
        return self.run_test(
            "Health Check (GET /api/)",
            "GET",
            "/api/",
            200
        )

    def test_create_status(self, client_name):
        """Test creating a status check"""
        return self.run_test(
            "Create Status Check (POST /api/status)",
            "POST",
            "/api/status",
            200,
            data={"client_name": client_name}
        )

    def test_get_status(self):
        """Test getting all status checks"""
        return self.run_test(
            "Get Status Checks (GET /api/status)",
            "GET",
            "/api/status",
            200
        )

def main():
    # Setup
    tester = StatusAPITester()
    test_client = f"test_client_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Run tests
    print("\n==== Testing Backend API ====")
    
    # Test health check
    health_success, health_data = tester.test_health_check()
    if not health_success:
        print("❌ Health check failed, stopping tests")
        return 1

    # Test creating a status check
    create_success, create_data = tester.test_create_status(test_client)
    if not create_success:
        print("❌ Status creation failed, stopping tests")
        return 1

    # Test getting status checks
    get_success, get_data = tester.test_get_status()
    if not get_success:
        print("❌ Status retrieval failed")
        return 1

    # Verify the created status is in the list
    if get_success:
        found = False
        for status in get_data:
            if status.get('client_name') == test_client:
                found = True
                break
        
        if found:
            print(f"✅ Successfully verified created status check for {test_client} in the list")
        else:
            print(f"❌ Could not find created status check for {test_client} in the list")
            tester.tests_passed -= 1

    # Print results
    print(f"\n📊 Tests passed: {tester.tests_passed}/{tester.tests_run}")
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())