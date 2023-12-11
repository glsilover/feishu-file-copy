# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListApplicationInterviewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.application_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListApplicationInterviewRequestBuilder":
        return ListApplicationInterviewRequestBuilder()


class ListApplicationInterviewRequestBuilder(object):

    def __init__(self) -> None:
        list_application_interview_request = ListApplicationInterviewRequest()
        list_application_interview_request.http_method = HttpMethod.GET
        list_application_interview_request.uri = "/open-apis/hire/v1/applications/:application_id/interviews"
        list_application_interview_request.token_types = {AccessTokenType.TENANT}
        self._list_application_interview_request: ListApplicationInterviewRequest = list_application_interview_request

    def page_size(self, page_size: int) -> "ListApplicationInterviewRequestBuilder":
        self._list_application_interview_request.page_size = page_size
        self._list_application_interview_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListApplicationInterviewRequestBuilder":
        self._list_application_interview_request.page_token = page_token
        self._list_application_interview_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListApplicationInterviewRequestBuilder":
        self._list_application_interview_request.user_id_type = user_id_type
        self._list_application_interview_request.add_query("user_id_type", user_id_type)
        return self

    def application_id(self, application_id: str) -> "ListApplicationInterviewRequestBuilder":
        self._list_application_interview_request.application_id = application_id
        self._list_application_interview_request.paths["application_id"] = str(application_id)
        return self

    def build(self) -> ListApplicationInterviewRequest:
        return self._list_application_interview_request
