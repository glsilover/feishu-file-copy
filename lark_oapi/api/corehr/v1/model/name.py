# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Name(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NameBuilder":
        return NameBuilder()


class NameBuilder(object):
    def __init__(self) -> None:
        self._name = Name()

    def zh_cn(self, zh_cn: str) -> "NameBuilder":
        self._name.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "NameBuilder":
        self._name.en_us = en_us
        return self

    def build(self) -> "Name":
        return self._name