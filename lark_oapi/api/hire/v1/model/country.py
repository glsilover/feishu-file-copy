# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Country(object):
    _types = {
        "country_code": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d=None):
        self.country_code: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CountryBuilder":
        return CountryBuilder()


class CountryBuilder(object):
    def __init__(self) -> None:
        self._country = Country()

    def country_code(self, country_code: str) -> "CountryBuilder":
        self._country.country_code = country_code
        return self

    def name(self, name: str) -> "CountryBuilder":
        self._country.name = name
        return self

    def en_name(self, en_name: str) -> "CountryBuilder":
        self._country.en_name = en_name
        return self

    def build(self) -> "Country":
        return self._country