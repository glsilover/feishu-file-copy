# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .weekday_schedule import WeekdaySchedule


class AgentScheduleUpdateInfo(object):
    _types = {
        "agent_id": str,
        "schedule": List[WeekdaySchedule],
        "agent_skill_ids": List[str],
    }

    def __init__(self, d=None):
        self.agent_id: Optional[str] = None
        self.schedule: Optional[List[WeekdaySchedule]] = None
        self.agent_skill_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgentScheduleUpdateInfoBuilder":
        return AgentScheduleUpdateInfoBuilder()


class AgentScheduleUpdateInfoBuilder(object):
    def __init__(self) -> None:
        self._agent_schedule_update_info = AgentScheduleUpdateInfo()

    def agent_id(self, agent_id: str) -> "AgentScheduleUpdateInfoBuilder":
        self._agent_schedule_update_info.agent_id = agent_id
        return self

    def schedule(self, schedule: List[WeekdaySchedule]) -> "AgentScheduleUpdateInfoBuilder":
        self._agent_schedule_update_info.schedule = schedule
        return self

    def agent_skill_ids(self, agent_skill_ids: List[str]) -> "AgentScheduleUpdateInfoBuilder":
        self._agent_schedule_update_info.agent_skill_ids = agent_skill_ids
        return self

    def build(self) -> "AgentScheduleUpdateInfo":
        return self._agent_schedule_update_info