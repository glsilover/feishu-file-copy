# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ApplicationStageTime(object):
    _types = {
        "stage_id": str,
        "enter_time": str,
        "exit_time": str,
    }

    def __init__(self, d=None):
        self.stage_id: Optional[str] = None
        self.enter_time: Optional[str] = None
        self.exit_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationStageTimeBuilder":
        return ApplicationStageTimeBuilder()


class ApplicationStageTimeBuilder(object):
    def __init__(self) -> None:
        self._application_stage_time = ApplicationStageTime()

    def stage_id(self, stage_id: str) -> "ApplicationStageTimeBuilder":
        self._application_stage_time.stage_id = stage_id
        return self

    def enter_time(self, enter_time: str) -> "ApplicationStageTimeBuilder":
        self._application_stage_time.enter_time = enter_time
        return self

    def exit_time(self, exit_time: str) -> "ApplicationStageTimeBuilder":
        self._application_stage_time.exit_time = exit_time
        return self

    def build(self) -> "ApplicationStageTime":
        return self._application_stage_time