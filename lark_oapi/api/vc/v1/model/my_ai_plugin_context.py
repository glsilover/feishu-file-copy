# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiPluginContext(object):
    _types = {
        "key": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiPluginContextBuilder":
        return MyAiPluginContextBuilder()


class MyAiPluginContextBuilder(object):
    def __init__(self) -> None:
        self._my_ai_plugin_context = MyAiPluginContext()

    def key(self, key: str) -> "MyAiPluginContextBuilder":
        self._my_ai_plugin_context.key = key
        return self

    def build(self) -> "MyAiPluginContext":
        return self._my_ai_plugin_context
