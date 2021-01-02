from app import app
from unittest import TestCase

app.config['WTF_CSRF_ENABLED'] = False

class SnackViewsTestCase(TestCase):
    """Tests for view functions for Snacks."""
    
    def test_snack_add_form(self):
        with app.test_client() as client:
            resp = client.get("/snacks/new")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<div class='container'", html)
            
    def test_snack_add(self):
        with app.test_client() as client:
            d = {"email": "caleb@mail.com", "name": "Test2", "quantity": 2, "price": 5.0, "category": "candy"}
            
            resp = client.post("/snacks/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 302)