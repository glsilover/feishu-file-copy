# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .enum import Enum


class Phone(object):
    _types = {
        "international_area_code": Enum,
        "phone_number": str,
        "formatted_phone_number": str,
        "device_type": Enum,
        "phone_usage": Enum,
        "is_primary": bool,
        "is_public": bool,
    }

    def __init__(self, d=None):
        self.international_area_code: Optional[Enum] = None
        self.phone_number: Optional[str] = None
        self.formatted_phone_number: Optional[str] = None
        self.device_type: Optional[Enum] = None
        self.phone_usage: Optional[Enum] = None
        self.is_primary: Optional[bool] = None
        self.is_public: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PhoneBuilder":
        return PhoneBuilder()


class PhoneBuilder(object):
    def __init__(self) -> None:
        self._phone = Phone()

    def international_area_code(self, international_area_code: Enum) -> "PhoneBuilder":
        self._phone.international_area_code = international_area_code
        return self

    def phone_number(self, phone_number: str) -> "PhoneBuilder":
        self._phone.phone_number = phone_number
        return self

    def formatted_phone_number(self, formatted_phone_number: str) -> "PhoneBuilder":
        self._phone.formatted_phone_number = formatted_phone_number
        return self

    def device_type(self, device_type: Enum) -> "PhoneBuilder":
        self._phone.device_type = device_type
        return self

    def phone_usage(self, phone_usage: Enum) -> "PhoneBuilder":
        self._phone.phone_usage = phone_usage
        return self

    def is_primary(self, is_primary: bool) -> "PhoneBuilder":
        self._phone.is_primary = is_primary
        return self

    def is_public(self, is_public: bool) -> "PhoneBuilder":
        self._phone.is_public = is_public
        return self

    def build(self) -> "Phone":
        return self._phone