.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :alt: website-contacts-py license
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/pypi/v/website-contacts.svg
    :alt: website-contacts-py release
    :target: https://pypi.org/project/website-contacts

.. image:: https://github.com/whois-api-llc/website-contacts-py/workflows/Build/badge.svg
    :alt: website-contacts-py build
    :target: https://github.com/whois-api-llc/website-contacts-py/actions

========
Overview
========

The client library for
`Website Contacts API <https://website-contacts.whoisxmlapi.com/>`_
in Python language.

The minimum Python version is 3.6.

Installation
============

.. code-block:: shell

    pip install website-contacts

Examples
========

Full API documentation available `here <https://website-contacts.whoisxmlapi.com/api/documentation/making-requests>`_

Create a new client
-------------------

.. code-block:: python

    from websitecontacts import *

    client = Client('Your API key')

Make basic requests
-------------------

.. code-block:: python

    # Get contacts for a domain name.
    response = client.get('youtube.com')
    print(response)

    # Get raw API response in XML format
    raw_result = client.get_raw('bbc.com',
        output_format=Client.XML_FORMAT)

Advanced usage
-------------------

Extra request parameters

.. code-block:: python

    result = client.get(
        'samsung.com',
        hard_refresh=True)

Response model overview
-----------------------

.. code-block:: python

    Response:
        - company_names: [str]
        - country_code: str
        - domain_name: str
        - emails: [Email]
            - description: str
            - email: str
        - meta_description: str
        - meta_title: str
        - phones: [Phone]
            - call_hours: str
            - description: str
            - phone_number: str
        - postal_addresses: [str]
        - social_facebook: str
        - social_instagram: str
        - social_linkedin: str
        - social_twitter: str
        - website_responded: bool


Sample response
---------------

.. code-block:: python

  {
  'company_names': [
                     'Samsung Electronics Co. Ltd',
                     'Samsung Electronics America Inc',
                     'Samsung-Sanyo Electronics',
                     'Samsung Electronics Industry Co Ltd',
                     'Samsung US'],
  'country_code': 'KR',
  'domain_name': 'samsung.com',
  'emails': [ {'description': '', 'email': 'ssvoc@samsung.com'},
              {'description': '', 'email': 'eco.sec@samsung.com'},
              {'description': '', 'email': 'ircontactus@samsung.com'}],
  'meta_description': 'Discover the latest in electronic & smart appliance '
                      'technology with Samsung. Find the next big thing from '
                      'smartphones & tablets to laptops & tvs & more.',
  'meta_title': 'Samsung US | Mobile | TV | Home Electronics | Home Appliances '
                '| Samsung US',
  'phones': [ {'call_hours': '', 'description': '', 'phone_number': '24 36 40'},
              {'call_hours': '', 'description': '', 'phone_number': '82-2-2255-9000'},
              {'call_hours': '8 AM - 12 AM EST 7 days a week IT/ Computing 8 AM to 9 PM EST Mon to Fri', 'description': '', 'phone_number': '1-800-SAMSUNG 726-7864'}],
  'postal_addresses': [],
  'social_facebook': 'https://www.facebook.com/SamsungUS',
  'social_instagram': 'https://instagram.com/samsungusa',
  'social_linkedin': '',
  'social_twitter': 'https://twitter.com/SamsungUS',
  'website_responded': True
  }
