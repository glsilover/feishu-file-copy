# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Calendar(object):
    _types = {
        "calendar_id": str,
        "summary": str,
        "description": str,
        "permissions": str,
        "color": int,
        "type": str,
        "summary_alias": str,
        "is_deleted": bool,
        "is_third_party": bool,
        "role": str,
    }

    def __init__(self, d=None):
        self.calendar_id: Optional[str] = None
        self.summary: Optional[str] = None
        self.description: Optional[str] = None
        self.permissions: Optional[str] = None
        self.color: Optional[int] = None
        self.type: Optional[str] = None
        self.summary_alias: Optional[str] = None
        self.is_deleted: Optional[bool] = None
        self.is_third_party: Optional[bool] = None
        self.role: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CalendarBuilder":
        return CalendarBuilder()


class CalendarBuilder(object):
    def __init__(self) -> None:
        self._calendar = Calendar()

    def calendar_id(self, calendar_id: str) -> "CalendarBuilder":
        self._calendar.calendar_id = calendar_id
        return self

    def summary(self, summary: str) -> "CalendarBuilder":
        self._calendar.summary = summary
        return self

    def description(self, description: str) -> "CalendarBuilder":
        self._calendar.description = description
        return self

    def permissions(self, permissions: str) -> "CalendarBuilder":
        self._calendar.permissions = permissions
        return self

    def color(self, color: int) -> "CalendarBuilder":
        self._calendar.color = color
        return self

    def type(self, type: str) -> "CalendarBuilder":
        self._calendar.type = type
        return self

    def summary_alias(self, summary_alias: str) -> "CalendarBuilder":
        self._calendar.summary_alias = summary_alias
        return self

    def is_deleted(self, is_deleted: bool) -> "CalendarBuilder":
        self._calendar.is_deleted = is_deleted
        return self

    def is_third_party(self, is_third_party: bool) -> "CalendarBuilder":
        self._calendar.is_third_party = is_third_party
        return self

    def role(self, role: str) -> "CalendarBuilder":
        self._calendar.role = role
        return self

    def build(self) -> "Calendar":
        return self._calendar
