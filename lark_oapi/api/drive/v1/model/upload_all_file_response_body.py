# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UploadAllFileResponseBody(object):
    _types = {
        "file_token": str,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadAllFileResponseBodyBuilder":
        return UploadAllFileResponseBodyBuilder()


class UploadAllFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_all_file_response_body = UploadAllFileResponseBody()

    def file_token(self, file_token: str) -> "UploadAllFileResponseBodyBuilder":
        self._upload_all_file_response_body.file_token = file_token
        return self

    def build(self) -> "UploadAllFileResponseBody":
        return self._upload_all_file_response_body
