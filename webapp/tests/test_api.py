import pytest
import requests

# Update this URL if testing against a deployed server
BASE_URL = "http://127.0.0.1:5000"

def test_hello_api():
    response = requests.get(f"{BASE_URL}/api")
    assert response.status_code == 200, "API did not return a 200 status code."
    data = response.json()
    assert "message" in data, "Response JSON does not contain 'message' key."
    assert data["message"] == "Hello, World!", "API message does not match expected output."

def test_invalid_route():
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404, "Invalid route should return 404 status code."
