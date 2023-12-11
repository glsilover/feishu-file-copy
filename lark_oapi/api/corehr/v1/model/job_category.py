# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class JobCategory(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobCategoryBuilder":
        return JobCategoryBuilder()


class JobCategoryBuilder(object):
    def __init__(self) -> None:
        self._job_category = JobCategory()

    def id(self, id: str) -> "JobCategoryBuilder":
        self._job_category.id = id
        return self

    def build(self) -> "JobCategory":
        return self._job_category