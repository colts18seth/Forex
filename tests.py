from currency_data import check_curr_code, get_curr_symbol
from app import app
from unittest import TestCase

class CurrencyTestCase(TestCase):
    """Forex unit tests."""

    def test_check_curr_code(self):
        self.assertTrue(check_curr_code("USD"))
        self.assertFalse(check_curr_code("US"))
    
    def test_get_curr_symbol(self):
        self.assertEqual(get_curr_symbol("USD"), "US$")
        self.assertNotEqual(get_curr_symbol("USD"), "$")

    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Forex Converter', html)

    def test_convert(self):
        with app.test_client() as client:
            resp = client.get('/convert?from=USD&to=EUR&amount=20.00')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('The result is:', html)
        
    def test_to_curr(self):
        with app.test_client() as client:
            resp = client.get('/convert?from=US&to=EUR&amount=20.00', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Invalid Currency Code!!', html)

    def test_from_curr(self):
        with app.test_client() as client:
            resp = client.get('/convert?from=USD&to=EU&amount=20.00', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Invalid Currency Code!!', html)

    def test_amount(self):
        with app.test_client() as client:
            resp = client.get('/convert?from=USD&to=EUR&amount=USD', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Invalid Currency Amount!!', html)

    def test_converter(self):
        with app.test_client() as client:
            resp = client.get('/convert?from=USD&to=USD&amount=1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('$ 1', html)