# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiResponsePresent(object):
    _types = {
        "type": str,
        "body": str,
        "interactable": bool,
        "operation_type": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.body: Optional[str] = None
        self.interactable: Optional[bool] = None
        self.operation_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiResponsePresentBuilder":
        return MyAiResponsePresentBuilder()


class MyAiResponsePresentBuilder(object):
    def __init__(self) -> None:
        self._my_ai_response_present = MyAiResponsePresent()

    def type(self, type: str) -> "MyAiResponsePresentBuilder":
        self._my_ai_response_present.type = type
        return self

    def body(self, body: str) -> "MyAiResponsePresentBuilder":
        self._my_ai_response_present.body = body
        return self

    def interactable(self, interactable: bool) -> "MyAiResponsePresentBuilder":
        self._my_ai_response_present.interactable = interactable
        return self

    def operation_type(self, operation_type: str) -> "MyAiResponsePresentBuilder":
        self._my_ai_response_present.operation_type = operation_type
        return self

    def build(self) -> "MyAiResponsePresent":
        return self._my_ai_response_present