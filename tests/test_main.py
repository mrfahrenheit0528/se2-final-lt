import pytest
from app.main import app  # Ensure 'app' is the name of your Flask instance

@pytest.fixture
def client():
    # This sets up a virtual browser for testing your tabulation app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    # Replace 'Tabulation' with a word that actually appears on your home screen
    assert b"Tabulation" in response.data 

def test_health_check(client):
    """Verifies the app is alive (useful for Task 3 deployment)."""
    # Note: You might need to add a /health route to your app.py as seen in the handout
    response = client.get('/health')
    if response.status_code == 404:
        pytest.skip("Health check route not implemented yet.")
    else:
        assert response.status_code == 200
        assert response.json == {"status": "ok"}