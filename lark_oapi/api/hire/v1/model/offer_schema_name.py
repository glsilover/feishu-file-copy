# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class OfferSchemaName(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferSchemaNameBuilder":
        return OfferSchemaNameBuilder()


class OfferSchemaNameBuilder(object):
    def __init__(self) -> None:
        self._offer_schema_name = OfferSchemaName()

    def zh_cn(self, zh_cn: str) -> "OfferSchemaNameBuilder":
        self._offer_schema_name.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "OfferSchemaNameBuilder":
        self._offer_schema_name.en_us = en_us
        return self

    def build(self) -> "OfferSchemaName":
        return self._offer_schema_name
