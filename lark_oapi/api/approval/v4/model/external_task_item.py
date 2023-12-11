# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ExternalTaskItem(object):
    _types = {
        "id": str,
        "status": str,
        "update_time": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.status: Optional[str] = None
        self.update_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExternalTaskItemBuilder":
        return ExternalTaskItemBuilder()


class ExternalTaskItemBuilder(object):
    def __init__(self) -> None:
        self._external_task_item = ExternalTaskItem()

    def id(self, id: str) -> "ExternalTaskItemBuilder":
        self._external_task_item.id = id
        return self

    def status(self, status: str) -> "ExternalTaskItemBuilder":
        self._external_task_item.status = status
        return self

    def update_time(self, update_time: int) -> "ExternalTaskItemBuilder":
        self._external_task_item.update_time = update_time
        return self

    def build(self) -> "ExternalTaskItem":
        return self._external_task_item