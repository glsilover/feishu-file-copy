# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .user_query_faq_info import UserQueryFaqInfo


class AnswerUserQueryTicketRequestBody(object):
    _types = {
        "event_id": str,
        "faqs": List[UserQueryFaqInfo],
    }

    def __init__(self, d=None):
        self.event_id: Optional[str] = None
        self.faqs: Optional[List[UserQueryFaqInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AnswerUserQueryTicketRequestBodyBuilder":
        return AnswerUserQueryTicketRequestBodyBuilder()


class AnswerUserQueryTicketRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._answer_user_query_ticket_request_body = AnswerUserQueryTicketRequestBody()

    def event_id(self, event_id: str) -> "AnswerUserQueryTicketRequestBodyBuilder":
        self._answer_user_query_ticket_request_body.event_id = event_id
        return self

    def faqs(self, faqs: List[UserQueryFaqInfo]) -> "AnswerUserQueryTicketRequestBodyBuilder":
        self._answer_user_query_ticket_request_body.faqs = faqs
        return self

    def build(self) -> "AnswerUserQueryTicketRequestBody":
        return self._answer_user_query_ticket_request_body
