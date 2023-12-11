# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .task import Task


class PatchTaskRequestBody(object):
    _types = {
        "task": Task,
        "update_fields": List[str],
    }

    def __init__(self, d=None):
        self.task: Optional[Task] = None
        self.update_fields: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchTaskRequestBodyBuilder":
        return PatchTaskRequestBodyBuilder()


class PatchTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_task_request_body = PatchTaskRequestBody()

    def task(self, task: Task) -> "PatchTaskRequestBodyBuilder":
        self._patch_task_request_body.task = task
        return self

    def update_fields(self, update_fields: List[str]) -> "PatchTaskRequestBodyBuilder":
        self._patch_task_request_body.update_fields = update_fields
        return self

    def build(self) -> "PatchTaskRequestBody":
        return self._patch_task_request_body
