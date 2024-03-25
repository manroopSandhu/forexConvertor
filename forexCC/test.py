from unittest import TestCase
from app import app 

class FlaskTests(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):

        with self.client:
            response = self.client.get('/')
            self.assertIn(b'<h1>Forex Currency', response.data)
            self.assertIn(b'<label>Converting from:', response.data)
            self.assertIn(b'<label>Converting to:', response.data)
            self.assertIn(b'<label>Amount:', response.data)

    def test_currency(self):
        
        with self.client:
            response1 = self.client.post('/', data={"converting-from": "USD", "converting-to": "USD", "amount": "1"})
            self.assertIn(b'<p>The Result Is $ 1.0</p>', response1.data)
            response2 = self.client.post('/', data={"converting-from": "USD", "converting-to": "EUR", "amount": "100"})
            self.assertIn(b'90.91</p>', response2.data)
            response3 = self.client.post('/', data={"converting-from": "USD", "converting-to": "INR", "amount": "6000"})
            self.assertIn(b'493200.0</p>', response3.data)