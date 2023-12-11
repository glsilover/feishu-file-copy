# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListApplicationFeedbackRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.from_date: Optional[str] = None
        self.to_date: Optional[str] = None
        self.feedback_type: Optional[int] = None
        self.status: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.page_token: Optional[int] = None
        self.page_size: Optional[int] = None
        self.app_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListApplicationFeedbackRequestBuilder":
        return ListApplicationFeedbackRequestBuilder()


class ListApplicationFeedbackRequestBuilder(object):

    def __init__(self) -> None:
        list_application_feedback_request = ListApplicationFeedbackRequest()
        list_application_feedback_request.http_method = HttpMethod.GET
        list_application_feedback_request.uri = "/open-apis/application/v6/applications/:app_id/feedbacks"
        list_application_feedback_request.token_types = {AccessTokenType.TENANT}
        self._list_application_feedback_request: ListApplicationFeedbackRequest = list_application_feedback_request

    def from_date(self, from_date: str) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.from_date = from_date
        self._list_application_feedback_request.add_query("from_date", from_date)
        return self

    def to_date(self, to_date: str) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.to_date = to_date
        self._list_application_feedback_request.add_query("to_date", to_date)
        return self

    def feedback_type(self, feedback_type: int) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.feedback_type = feedback_type
        self._list_application_feedback_request.add_query("feedback_type", feedback_type)
        return self

    def status(self, status: int) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.status = status
        self._list_application_feedback_request.add_query("status", status)
        return self

    def user_id_type(self, user_id_type: str) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.user_id_type = user_id_type
        self._list_application_feedback_request.add_query("user_id_type", user_id_type)
        return self

    def page_token(self, page_token: int) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.page_token = page_token
        self._list_application_feedback_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.page_size = page_size
        self._list_application_feedback_request.add_query("page_size", page_size)
        return self

    def app_id(self, app_id: str) -> "ListApplicationFeedbackRequestBuilder":
        self._list_application_feedback_request.app_id = app_id
        self._list_application_feedback_request.paths["app_id"] = str(app_id)
        return self

    def build(self) -> ListApplicationFeedbackRequest:
        return self._list_application_feedback_request
