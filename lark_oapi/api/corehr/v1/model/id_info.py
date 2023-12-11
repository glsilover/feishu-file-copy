# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class IdInfo(object):
    _types = {
        "id": str,
        "target_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.target_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "IdInfoBuilder":
        return IdInfoBuilder()


class IdInfoBuilder(object):
    def __init__(self) -> None:
        self._id_info = IdInfo()

    def id(self, id: str) -> "IdInfoBuilder":
        self._id_info.id = id
        return self

    def target_id(self, target_id: str) -> "IdInfoBuilder":
        self._id_info.target_id = target_id
        return self

    def build(self) -> "IdInfo":
        return self._id_info