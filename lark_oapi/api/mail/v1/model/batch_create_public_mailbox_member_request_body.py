# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .public_mailbox_member import PublicMailboxMember


class BatchCreatePublicMailboxMemberRequestBody(object):
    _types = {
        "items": List[PublicMailboxMember],
    }

    def __init__(self, d=None):
        self.items: Optional[List[PublicMailboxMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreatePublicMailboxMemberRequestBodyBuilder":
        return BatchCreatePublicMailboxMemberRequestBodyBuilder()


class BatchCreatePublicMailboxMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_public_mailbox_member_request_body = BatchCreatePublicMailboxMemberRequestBody()

    def items(self, items: List[PublicMailboxMember]) -> "BatchCreatePublicMailboxMemberRequestBodyBuilder":
        self._batch_create_public_mailbox_member_request_body.items = items
        return self

    def build(self) -> "BatchCreatePublicMailboxMemberRequestBody":
        return self._batch_create_public_mailbox_member_request_body
