import requests
import json

# Base URL of your FastAPI application
BASE_URL = "http://localhost:8000"  # Adjust this if your server is running on a different port

def test_register(username, password):
    url = f"{BASE_URL}/register"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    print(f"Registration Response: {response.status_code}")
    print(response.json())
    return response.status_code == 201

def test_login(username, password):
    url = f"{BASE_URL}/token"
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    print(f"Login Response: {response.status_code}")
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(response.json())
        return None

def test_protected_route(token):
    url = f"{BASE_URL}/protected"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"Protected Route Response: {response.status_code}")
    print(response.json())

def test_get_user_info(token):
    url = f"{BASE_URL}/users/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"User Info Response: {response.status_code}")
    print(response.json())

def main():
    username = "testuser"
    password = "testpassword"

    # Test registration
    if test_register(username, password):
        print("Registration successful")
    else:
        print("Registration failed")

    # Test login
    token = test_login(username, password)
    if token:
        print("Login successful")
        
        # Test protected route
        test_protected_route(token)
        
        # Test get user info
        test_get_user_info(token)
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
