# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .calendar import Calendar


class UserCalendar(object):
    _types = {
        "calendar": Calendar,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.calendar: Optional[Calendar] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserCalendarBuilder":
        return UserCalendarBuilder()


class UserCalendarBuilder(object):
    def __init__(self) -> None:
        self._user_calendar = UserCalendar()

    def calendar(self, calendar: Calendar) -> "UserCalendarBuilder":
        self._user_calendar.calendar = calendar
        return self

    def user_id(self, user_id: str) -> "UserCalendarBuilder":
        self._user_calendar.user_id = user_id
        return self

    def build(self) -> "UserCalendar":
        return self._user_calendar