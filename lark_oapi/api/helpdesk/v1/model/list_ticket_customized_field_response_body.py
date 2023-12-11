# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .ticket_customized_field import TicketCustomizedField


class ListTicketCustomizedFieldResponseBody(object):
    _types = {
        "has_more": bool,
        "next_page_token": str,
        "items": List[TicketCustomizedField],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.next_page_token: Optional[str] = None
        self.items: Optional[List[TicketCustomizedField]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTicketCustomizedFieldResponseBodyBuilder":
        return ListTicketCustomizedFieldResponseBodyBuilder()


class ListTicketCustomizedFieldResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_ticket_customized_field_response_body = ListTicketCustomizedFieldResponseBody()

    def has_more(self, has_more: bool) -> "ListTicketCustomizedFieldResponseBodyBuilder":
        self._list_ticket_customized_field_response_body.has_more = has_more
        return self

    def next_page_token(self, next_page_token: str) -> "ListTicketCustomizedFieldResponseBodyBuilder":
        self._list_ticket_customized_field_response_body.next_page_token = next_page_token
        return self

    def items(self, items: List[TicketCustomizedField]) -> "ListTicketCustomizedFieldResponseBodyBuilder":
        self._list_ticket_customized_field_response_body.items = items
        return self

    def build(self) -> "ListTicketCustomizedFieldResponseBody":
        return self._list_ticket_customized_field_response_body