# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .enum import Enum
from .i18n import I18n


class Subdivision(object):
    _types = {
        "id": str,
        "name": List[I18n],
        "country_region_id": str,
        "subdivision_type": Enum,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.country_region_id: Optional[str] = None
        self.subdivision_type: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubdivisionBuilder":
        return SubdivisionBuilder()


class SubdivisionBuilder(object):
    def __init__(self) -> None:
        self._subdivision = Subdivision()

    def id(self, id: str) -> "SubdivisionBuilder":
        self._subdivision.id = id
        return self

    def name(self, name: List[I18n]) -> "SubdivisionBuilder":
        self._subdivision.name = name
        return self

    def country_region_id(self, country_region_id: str) -> "SubdivisionBuilder":
        self._subdivision.country_region_id = country_region_id
        return self

    def subdivision_type(self, subdivision_type: Enum) -> "SubdivisionBuilder":
        self._subdivision.subdivision_type = subdivision_type
        return self

    def build(self) -> "Subdivision":
        return self._subdivision
