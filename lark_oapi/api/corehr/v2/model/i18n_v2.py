# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class I18nV2(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nV2Builder":
        return I18nV2Builder()


class I18nV2Builder(object):
    def __init__(self) -> None:
        self._i18n_v2 = I18nV2()

    def zh_cn(self, zh_cn: str) -> "I18nV2Builder":
        self._i18n_v2.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "I18nV2Builder":
        self._i18n_v2.en_us = en_us
        return self

    def build(self) -> "I18nV2":
        return self._i18n_v2
