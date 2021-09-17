import os
import unittest
from websitecontacts import Client
from websitecontacts import ParameterError, ApiAuthError

domains = ['youtube.com', 'bbc.com', 'google.com']
invalid_domain = '345.#ab.%org'


class TestClient(unittest.TestCase):
    """
    Final integration tests without mocks.

    Active API_KEY is required.
    """
    def setUp(self) -> None:
        self.client = Client(os.getenv('API_KEY'))

    def test_get_correct_data(self):
        response = self.client.get(domain=domains[0])
        self.assertRegex(response.meta_description.lower(), domains[0].split('.', 1)[0])

    def test_invalid_domain(self):
        with self.assertRaises(ParameterError):
            self.client.get(invalid_domain)

    def test_incorrect_api_key(self):
        client = Client('at_00000000000000000000000000000')
        with self.assertRaises(ApiAuthError):
            client.get(domain=domains[1])

    def test_raw_data(self):
        response = self.client.get_raw(
            domain=domains[0], output_format=Client.XML_FORMAT)
        self.assertTrue(response.startswith('<?xml'))


if __name__ == '__main__':
    unittest.main()
