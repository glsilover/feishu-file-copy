# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BackgroundCheckCity(object):
    _types = {
        "zh_cn": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckCityBuilder":
        return BackgroundCheckCityBuilder()


class BackgroundCheckCityBuilder(object):
    def __init__(self) -> None:
        self._background_check_city = BackgroundCheckCity()

    def zh_cn(self, zh_cn: str) -> "BackgroundCheckCityBuilder":
        self._background_check_city.zh_cn = zh_cn
        return self

    def en_us(self, en_us: str) -> "BackgroundCheckCityBuilder":
        self._background_check_city.en_us = en_us
        return self

    def build(self) -> "BackgroundCheckCity":
        return self._background_check_city