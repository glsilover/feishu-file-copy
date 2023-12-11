# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetCalendarEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.need_meeting_settings: Optional[bool] = None
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCalendarEventRequestBuilder":
        return GetCalendarEventRequestBuilder()


class GetCalendarEventRequestBuilder(object):

    def __init__(self) -> None:
        get_calendar_event_request = GetCalendarEventRequest()
        get_calendar_event_request.http_method = HttpMethod.GET
        get_calendar_event_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id"
        get_calendar_event_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_calendar_event_request: GetCalendarEventRequest = get_calendar_event_request

    def need_meeting_settings(self, need_meeting_settings: bool) -> "GetCalendarEventRequestBuilder":
        self._get_calendar_event_request.need_meeting_settings = need_meeting_settings
        self._get_calendar_event_request.add_query("need_meeting_settings", need_meeting_settings)
        return self

    def user_id_type(self, user_id_type: str) -> "GetCalendarEventRequestBuilder":
        self._get_calendar_event_request.user_id_type = user_id_type
        self._get_calendar_event_request.add_query("user_id_type", user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "GetCalendarEventRequestBuilder":
        self._get_calendar_event_request.calendar_id = calendar_id
        self._get_calendar_event_request.paths["calendar_id"] = str(calendar_id)
        return self

    def event_id(self, event_id: str) -> "GetCalendarEventRequestBuilder":
        self._get_calendar_event_request.event_id = event_id
        self._get_calendar_event_request.paths["event_id"] = str(event_id)
        return self

    def build(self) -> GetCalendarEventRequest:
        return self._get_calendar_event_request