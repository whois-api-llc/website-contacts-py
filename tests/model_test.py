import json
import unittest
from json import loads
from websitecontacts import Response, ErrorMessage

_json_response_ok = '''{
    "companyNames": [
        "Google LLC D/B/A YouTube",
        "YouTube Community Guidelines & Policies",
        "Google Inc",
        "Brand Resources"
    ],
    "countryCode": "US",
    "domainName": "youtube.com",
    "emails": [
        {
            "description": "Press",
            "email": "press@google.com"
        },
        {
            "description": "Support",
            "email": "support@google.com"
        }
    ],
    "meta": {
        "description": "Enjoy the videos and music you love, upload\
         original content, and share it all with friends, family, and the world on YouTube.",
        "title": "YouTube"
    },
    "phones": [
        {
            "callHours": "",
            "description": "",
            "phoneNumber": "650-253-0001"
        },
        {
            "callHours": "10:00-19:00",
            "description": "",
            "phoneNumber": "650-253-0002"
        }
    ],
    "postalAddresses": [
        "901 Cherry Ave. San Bruno CA 94066 USA"
    ],
    "socialLinks": {
        "facebook": "https://www.facebook.com/youtube/?ref=br_r",
        "instagram": "https://www.instagram.com/youtube/",
        "linkedIn": "",
        "twitter": "https://twitter.com/YouTube"
    },
    "websiteResponded": true
}'''

_json_response_error = '''{
    "code": 403,
    "messages": "Access restricted. Check credits balance or enter the correct API key."
}'''


class TestModel(unittest.TestCase):

    def test_response_parsing(self):
        response = loads(_json_response_ok)
        parsed = Response(response)
        self.assertIsInstance(parsed.company_names, list)
        self.assertListEqual(parsed.company_names, response['companyNames'])
        self.assertEqual(parsed.country_code, response['countryCode'])
        self.assertEqual(parsed.domain_name, response['domainName'])
        self.assertIsInstance(parsed.emails, list)
        self.assertDictEqual(vars(parsed.emails[0]), response['emails'][0])
        self.assertDictEqual(vars(parsed.emails[1]), response['emails'][1])

        self.assertEqual(parsed.meta_description, response['meta']['description'])
        self.assertEqual(parsed.meta_title, response['meta']['title'])

        self.assertIsInstance(parsed.phones, list)
        self.assertEqual(parsed.phones[0].call_hours, response['phones'][0]['callHours'])
        self.assertEqual(parsed.phones[0].description, response['phones'][0]['description'])
        self.assertEqual(parsed.phones[0].phone_number, response['phones'][0]['phoneNumber'])
        self.assertEqual(parsed.phones[1].call_hours, response['phones'][1]['callHours'])
        self.assertEqual(parsed.phones[1].description, response['phones'][1]['description'])
        self.assertEqual(parsed.phones[1].phone_number, response['phones'][1]['phoneNumber'])

        self.assertIsInstance(parsed.postal_addresses, list)
        self.assertListEqual(parsed.postal_addresses, response['postalAddresses'])

        self.assertEqual(parsed.social_facebook, response['socialLinks']['facebook'])
        self.assertEqual(parsed.social_instagram, response['socialLinks']['instagram'])
        self.assertEqual(parsed.social_linkedin, response['socialLinks']['linkedIn'])
        self.assertEqual(parsed.social_twitter, response['socialLinks']['twitter'])
        self.assertEqual(parsed.website_responded, response['websiteResponded'])

    def test_error_parsing(self):
        error = loads(_json_response_error)
        parsed_error = ErrorMessage(error)
        self.assertEqual(parsed_error.code, error['code'])
        self.assertEqual(parsed_error.message, error['messages'])

    def test_comparing_two_models(self):
        model1 = Response(json.loads(_json_response_ok))
        model2 = Response(json.loads(_json_response_ok))
        self.assertEqual(model1, model2)
