import copy
from datetime import datetime

from .base import BaseModel
import sys

if sys.version_info < (3, 9):
    import typing


def _datetime_from_int(values: dict, key: str) -> datetime or None:
    if key in values and values[key]:
        return datetime.utcfromtimestamp(values[key])
    return None


def _string_value(values: dict, key: str) -> str:
    if key in values and values[key]:
        return str(values[key])
    return ''


def _float_value(values: dict, key: str) -> float:
    if key in values and values[key]:
        return float(values[key])
    return 0.0


def _int_value(values: dict, key: str) -> int:
    if key in values and values[key]:
        return int(values[key])
    return 0


def _list_value(values: dict, key: str) -> list:
    if key in values and type(values[key]) is list:
        return copy.deepcopy(values[key])
    return []


def _list_of_objects(values: dict, key: str, classname: str) -> list:
    r = []
    if key in values and type(values[key]) is list:
        r = [globals()[classname](x) for x in values[key]]
    return r


def _bool_value(values: dict, key: str) -> bool:
    if key in values and values[key]:
        return bool(values[key])
    return False


class Email(BaseModel):
    description: str
    email: str

    def __init__(self, values):
        super().__init__()
        self.description = ''
        self.email = ''

        if values:
            self.description = _string_value(values, 'description')
            self.email = _string_value(values, 'email')


class Phone(BaseModel):
    call_hours: str
    description: str
    phone_number: str

    def __init__(self, values):
        super().__init__()
        self.call_hours = ''
        self.description = ''
        self.phone_number = ''

        if values:
            self.call_hours = _string_value(values, 'callHours')
            self.description = _string_value(values, 'description')
            self.phone_number = _string_value(values, 'phoneNumber')


class Response(BaseModel):
    company_names: [str]
    country_code: str
    domain_name: str
    if sys.version_info < (3, 9):
        emails: typing.List[Email]
        phones: typing.List[Phone]
    else:
        emails: [Email]
        phones: [Phone]

    def __init__(self, values):
        super().__init__()
        self.company_names = []
        self.country_code = ''
        self.domain_name = ''
        self.emails = []
        self.meta_description = ''
        self.meta_title = ''
        self.phones = []
        self.postal_addresses = []
        self.social_facebook = ''
        self.social_instagram = ''
        self.social_linkedin = ''
        self.social_twitter = ''
        self.website_responded = False

        if values is not None:
            self.company_names = _list_value(values, 'companyNames')
            self.country_code = _string_value(values, 'countryCode')
            self.domain_name = _string_value(values, 'domainName')
            self.emails = _list_of_objects(values, 'emails', 'Email')
            self.meta_description = _string_value(values['meta'], 'description')
            self.meta_title = _string_value(values['meta'], 'title')
            self.phones = _list_of_objects(values, 'phones', 'Phone')
            self.postal_addresses = _list_value(values, 'postalAddresses')
            social = values['socialLinks']
            if 'facebook' in social:
                self.social_facebook = _string_value(social, 'facebook')
            if 'instagram' in social:
                self.social_instagram = _string_value(social, 'instagram')
            if 'linkedIn' in social:
                self.social_linkedin = _string_value(social, 'linkedIn')
            if 'twitter' in social:
                self.social_twitter = _string_value(social, 'twitter')
            self.website_responded = _bool_value(values, 'websiteResponded')


class ErrorMessage(BaseModel):
    code: int
    message: str

    def __init__(self, values):
        super().__init__()

        self.code = 0
        self.message = ''

        if values is not None:
            self.code = _int_value(values, 'code')
            self.message = _string_value(values, 'messages')
