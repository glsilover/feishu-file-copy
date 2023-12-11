# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class EventTime(object):
    _types = {
        "time_stamp": str,
    }

    def __init__(self, d=None):
        self.time_stamp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventTimeBuilder":
        return EventTimeBuilder()


class EventTimeBuilder(object):
    def __init__(self) -> None:
        self._event_time = EventTime()

    def time_stamp(self, time_stamp: str) -> "EventTimeBuilder":
        self._event_time.time_stamp = time_stamp
        return self

    def build(self) -> "EventTime":
        return self._event_time
