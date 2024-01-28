import unittest
from flask import Flask
import helloworld

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = helloworld.app.test_client()

    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_home_route(self):
        name = 'Sterling Archer'
        response = self.app.get(f'/home/{name}')
        self.assertEqual(response.status_code, 200)
        expected_html = f'<h1>Hello {name}!</h1>'
        self.assertEqual(response.data.decode('utf-8'), expected_html)

if __name__ == '__main__':
    unittest.main()
