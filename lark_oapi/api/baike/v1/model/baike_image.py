# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BaikeImage(object):
    _types = {
        "token": str,
    }

    def __init__(self, d=None):
        self.token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BaikeImageBuilder":
        return BaikeImageBuilder()


class BaikeImageBuilder(object):
    def __init__(self) -> None:
        self._baike_image = BaikeImage()

    def token(self, token: str) -> "BaikeImageBuilder":
        self._baike_image.token = token
        return self

    def build(self) -> "BaikeImage":
        return self._baike_image
