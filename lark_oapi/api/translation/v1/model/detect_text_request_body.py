# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DetectTextRequestBody(object):
    _types = {
        "text": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DetectTextRequestBodyBuilder":
        return DetectTextRequestBodyBuilder()


class DetectTextRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._detect_text_request_body = DetectTextRequestBody()

    def text(self, text: str) -> "DetectTextRequestBodyBuilder":
        self._detect_text_request_body.text = text
        return self

    def build(self) -> "DetectTextRequestBody":
        return self._detect_text_request_body