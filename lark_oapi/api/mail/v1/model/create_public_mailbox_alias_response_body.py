# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .email_alias import EmailAlias


class CreatePublicMailboxAliasResponseBody(object):
    _types = {
        "public_mailbox_alias": EmailAlias,
    }

    def __init__(self, d=None):
        self.public_mailbox_alias: Optional[EmailAlias] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreatePublicMailboxAliasResponseBodyBuilder":
        return CreatePublicMailboxAliasResponseBodyBuilder()


class CreatePublicMailboxAliasResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_public_mailbox_alias_response_body = CreatePublicMailboxAliasResponseBody()

    def public_mailbox_alias(self, public_mailbox_alias: EmailAlias) -> "CreatePublicMailboxAliasResponseBodyBuilder":
        self._create_public_mailbox_alias_response_body.public_mailbox_alias = public_mailbox_alias
        return self

    def build(self) -> "CreatePublicMailboxAliasResponseBody":
        return self._create_public_mailbox_alias_response_body
