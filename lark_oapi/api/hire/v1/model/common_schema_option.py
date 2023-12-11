# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n


class CommonSchemaOption(object):
    _types = {
        "key": str,
        "name": I18n,
        "description": I18n,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonSchemaOptionBuilder":
        return CommonSchemaOptionBuilder()


class CommonSchemaOptionBuilder(object):
    def __init__(self) -> None:
        self._common_schema_option = CommonSchemaOption()

    def key(self, key: str) -> "CommonSchemaOptionBuilder":
        self._common_schema_option.key = key
        return self

    def name(self, name: I18n) -> "CommonSchemaOptionBuilder":
        self._common_schema_option.name = name
        return self

    def description(self, description: I18n) -> "CommonSchemaOptionBuilder":
        self._common_schema_option.description = description
        return self

    def active_status(self, active_status: int) -> "CommonSchemaOptionBuilder":
        self._common_schema_option.active_status = active_status
        return self

    def build(self) -> "CommonSchemaOption":
        return self._common_schema_option
