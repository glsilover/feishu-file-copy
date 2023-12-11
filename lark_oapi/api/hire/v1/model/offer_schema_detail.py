# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .offer_schema_detail_option import OfferSchemaDetailOption
from .offer_schema_name import OfferSchemaName


class OfferSchemaDetail(object):
    _types = {
        "id": str,
        "name": OfferSchemaName,
        "type": str,
        "is_customized": bool,
        "option_list": List[OfferSchemaDetailOption],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[OfferSchemaName] = None
        self.type: Optional[str] = None
        self.is_customized: Optional[bool] = None
        self.option_list: Optional[List[OfferSchemaDetailOption]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferSchemaDetailBuilder":
        return OfferSchemaDetailBuilder()


class OfferSchemaDetailBuilder(object):
    def __init__(self) -> None:
        self._offer_schema_detail = OfferSchemaDetail()

    def id(self, id: str) -> "OfferSchemaDetailBuilder":
        self._offer_schema_detail.id = id
        return self

    def name(self, name: OfferSchemaName) -> "OfferSchemaDetailBuilder":
        self._offer_schema_detail.name = name
        return self

    def type(self, type: str) -> "OfferSchemaDetailBuilder":
        self._offer_schema_detail.type = type
        return self

    def is_customized(self, is_customized: bool) -> "OfferSchemaDetailBuilder":
        self._offer_schema_detail.is_customized = is_customized
        return self

    def option_list(self, option_list: List[OfferSchemaDetailOption]) -> "OfferSchemaDetailBuilder":
        self._offer_schema_detail.option_list = option_list
        return self

    def build(self) -> "OfferSchemaDetail":
        return self._offer_schema_detail