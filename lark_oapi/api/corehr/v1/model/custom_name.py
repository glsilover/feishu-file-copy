# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class CustomName(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomNameBuilder":
        return CustomNameBuilder()


class CustomNameBuilder(object):
    def __init__(self) -> None:
        self._custom_name = CustomName()

    def zh_cn(self, zh_cn: str) -> "CustomNameBuilder":
        self._custom_name.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "CustomNameBuilder":
        self._custom_name.en_us = en_us
        return self

    def build(self) -> "CustomName":
        return self._custom_name
