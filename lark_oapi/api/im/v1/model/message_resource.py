# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class MessageResource(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageResourceBuilder":
        return MessageResourceBuilder()


class MessageResourceBuilder(object):
    def __init__(self) -> None:
        self._message_resource = MessageResource()

    def build(self) -> "MessageResource":
        return self._message_resource
