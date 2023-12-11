# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .common_schema_option import CommonSchemaOption


class CommonSchemaConfig(object):
    _types = {
        "options": List[CommonSchemaOption],
    }

    def __init__(self, d=None):
        self.options: Optional[List[CommonSchemaOption]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommonSchemaConfigBuilder":
        return CommonSchemaConfigBuilder()


class CommonSchemaConfigBuilder(object):
    def __init__(self) -> None:
        self._common_schema_config = CommonSchemaConfig()

    def options(self, options: List[CommonSchemaOption]) -> "CommonSchemaConfigBuilder":
        self._common_schema_config.options = options
        return self

    def build(self) -> "CommonSchemaConfig":
        return self._common_schema_config
