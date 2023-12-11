# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ProgressRecordSimplify(object):
    _types = {
        "id": int,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProgressRecordSimplifyBuilder":
        return ProgressRecordSimplifyBuilder()


class ProgressRecordSimplifyBuilder(object):
    def __init__(self) -> None:
        self._progress_record_simplify = ProgressRecordSimplify()

    def id(self, id: int) -> "ProgressRecordSimplifyBuilder":
        self._progress_record_simplify.id = id
        return self

    def build(self) -> "ProgressRecordSimplify":
        return self._progress_record_simplify
