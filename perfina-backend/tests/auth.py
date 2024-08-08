import requests
import json
import tempfile
import os

# Base URL of your FastAPI application
BASE_URL = (
    "http://localhost:8000"  # Adjust this if your server is running on a different port
)


def test_register(username, password):
    # Test user registration
    url = f"{BASE_URL}/register"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    print(f"Registration Response: {response.status_code}")
    print(response.json())
    return response.status_code == 201


def test_login(username, password):
    # Test user login and token retrieval
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
    # Test access to a protected route
    url = f"{BASE_URL}/protected"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"Protected Route Response: {response.status_code}")
    print(response.json())


def test_get_user_info(token):
    # Test retrieval of user information
    url = f"{BASE_URL}/users/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"User Info Response: {response.status_code}")
    print(response.json())


def test_generate_invoice(token):
    # Test invoice generation
    url = f"{BASE_URL}/generate-invoice"
    #headers = {"Authorization": f"Bearer {token}"}
    data = {
        "company_name": "SAIGON Technologies s.r.o",
        "company_address": "Klášterecká 1051/28",
        "company_postal_code": "184 00 Praha",
        "company_phone": "+420 720 975 950",
        "company_email": "saigon-tech@tuta.io",
        "company_ico": "04317114",
        "company_dic": "CZ04317114",
        "company_bank_account": "2902834310/2010",
        "category": "IT Služby",
        "services": "Tvorba softwaru a správa Linux serverů",
        "rate": 320,
        "hours": 260,
        "invoice_number": 2024002,
        "variable_symbol": "00000002",
        "invoice_date": "29.4.2024",
        "invoice_due": "15.5.2024",
        "client_name": "IDC-softwarehouse, s.r.o.",
        "client_address": "U Průhonu 773/12",
        "client_postal_code": "170 00 Praha",
        "client_ico": "26204576",
        "client_dic": "CZ26204576",
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"Invoice Generation Response: {response.status_code}")

    if response.status_code == 200:
        # Create a temporary file to save the PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(response.content)
            tmp_file_path = tmp_file.name

        print(f"Invoice PDF saved temporarily at: {tmp_file_path}")
        print("Please check the PDF file to ensure it was generated correctly.")

        # Optionally, you can open the PDF file automatically
        # Uncomment the following lines if you want this functionality
        # import subprocess
        # subprocess.run(['open', tmp_file_path], check=True)
    else:
        print("Failed to generate invoice")
        print(response.text)


def main():
    username = "testuser@test.com"
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

        # Test invoice generation
        test_generate_invoice(token)
    else:
        print("Login failed")


if __name__ == "__main__":
    main()
