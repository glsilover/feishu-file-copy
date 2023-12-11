# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class JobLevel(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobLevelBuilder":
        return JobLevelBuilder()


class JobLevelBuilder(object):
    def __init__(self) -> None:
        self._job_level = JobLevel()

    def id(self, id: str) -> "JobLevelBuilder":
        self._job_level.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobLevelBuilder":
        self._job_level.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobLevelBuilder":
        self._job_level.en_name = en_name
        return self

    def active_status(self, active_status: int) -> "JobLevelBuilder":
        self._job_level.active_status = active_status
        return self

    def build(self) -> "JobLevel":
        return self._job_level
