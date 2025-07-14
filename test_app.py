import unittest
from app import app  # Import the Flask app from the app.py file

class FlaskTestCase(unittest.TestCase):
    
    # Set up the testing environment
    def setUp(self):
        # The `test_client` allows us to send HTTP requests to the app
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode

    # Test the homepage
    def test_home(self):
        # Use the test client to send a GET request to the home page
        response = self.app.get('/')
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response data matches the expected "Hello, World!"
        self.assertEqual(response.data.decode(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
