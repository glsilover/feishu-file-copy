# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class AppCustomCategoryI18nInfo(object):
    _types = {
        "i18n_key": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.i18n_key: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppCustomCategoryI18nInfoBuilder":
        return AppCustomCategoryI18nInfoBuilder()


class AppCustomCategoryI18nInfoBuilder(object):
    def __init__(self) -> None:
        self._app_custom_category_i18n_info = AppCustomCategoryI18nInfo()

    def i18n_key(self, i18n_key: str) -> "AppCustomCategoryI18nInfoBuilder":
        self._app_custom_category_i18n_info.i18n_key = i18n_key
        return self

    def name(self, name: str) -> "AppCustomCategoryI18nInfoBuilder":
        self._app_custom_category_i18n_info.name = name
        return self

    def build(self) -> "AppCustomCategoryI18nInfo":
        return self._app_custom_category_i18n_info
