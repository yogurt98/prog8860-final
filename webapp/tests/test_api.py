import pytest
from webapp.app import app  # Import your Flask app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello_api(client):
    # Use the test client to send a GET request
    response = client.get('/api')
    assert response.status_code == 200  # Check if status code is 200
    data = response.get_json()  # Parse the JSON response
    assert data == {"message": "Hello, World!"}  # Validate the response
