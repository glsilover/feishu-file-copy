# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ReportMeetingDaily(object):
    _types = {
        "date": int,
        "meeting_count": int,
        "meeting_duration": int,
        "participant_count": int,
    }

    def __init__(self, d=None):
        self.date: Optional[int] = None
        self.meeting_count: Optional[int] = None
        self.meeting_duration: Optional[int] = None
        self.participant_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReportMeetingDailyBuilder":
        return ReportMeetingDailyBuilder()


class ReportMeetingDailyBuilder(object):
    def __init__(self) -> None:
        self._report_meeting_daily = ReportMeetingDaily()

    def date(self, date: int) -> "ReportMeetingDailyBuilder":
        self._report_meeting_daily.date = date
        return self

    def meeting_count(self, meeting_count: int) -> "ReportMeetingDailyBuilder":
        self._report_meeting_daily.meeting_count = meeting_count
        return self

    def meeting_duration(self, meeting_duration: int) -> "ReportMeetingDailyBuilder":
        self._report_meeting_daily.meeting_duration = meeting_duration
        return self

    def participant_count(self, participant_count: int) -> "ReportMeetingDailyBuilder":
        self._report_meeting_daily.participant_count = participant_count
        return self

    def build(self) -> "ReportMeetingDaily":
        return self._report_meeting_daily
