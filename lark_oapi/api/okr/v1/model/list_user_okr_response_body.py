# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .okr_batch import OkrBatch


class ListUserOkrResponseBody(object):
    _types = {
        "total": int,
        "okr_list": List[OkrBatch],
    }

    def __init__(self, d=None):
        self.total: Optional[int] = None
        self.okr_list: Optional[List[OkrBatch]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListUserOkrResponseBodyBuilder":
        return ListUserOkrResponseBodyBuilder()


class ListUserOkrResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_user_okr_response_body = ListUserOkrResponseBody()

    def total(self, total: int) -> "ListUserOkrResponseBodyBuilder":
        self._list_user_okr_response_body.total = total
        return self

    def okr_list(self, okr_list: List[OkrBatch]) -> "ListUserOkrResponseBodyBuilder":
        self._list_user_okr_response_body.okr_list = okr_list
        return self

    def build(self) -> "ListUserOkrResponseBody":
        return self._list_user_okr_response_body