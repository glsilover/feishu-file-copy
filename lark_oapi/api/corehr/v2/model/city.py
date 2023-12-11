# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .i18n import I18n


class City(object):
    _types = {
        "city_id": str,
        "name": List[I18n],
        "country_region_subdivision_id": str,
        "code": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.city_id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.country_region_subdivision_id: Optional[str] = None
        self.code: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CityBuilder":
        return CityBuilder()


class CityBuilder(object):
    def __init__(self) -> None:
        self._city = City()

    def city_id(self, city_id: str) -> "CityBuilder":
        self._city.city_id = city_id
        return self

    def name(self, name: List[I18n]) -> "CityBuilder":
        self._city.name = name
        return self

    def country_region_subdivision_id(self, country_region_subdivision_id: str) -> "CityBuilder":
        self._city.country_region_subdivision_id = country_region_subdivision_id
        return self

    def code(self, code: str) -> "CityBuilder":
        self._city.code = code
        return self

    def status(self, status: int) -> "CityBuilder":
        self._city.status = status
        return self

    def build(self) -> "City":
        return self._city