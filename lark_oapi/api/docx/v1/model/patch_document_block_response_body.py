# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .block import Block


class PatchDocumentBlockResponseBody(object):
    _types = {
        "block": Block,
        "document_revision_id": int,
        "client_token": str,
    }

    def __init__(self, d=None):
        self.block: Optional[Block] = None
        self.document_revision_id: Optional[int] = None
        self.client_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchDocumentBlockResponseBodyBuilder":
        return PatchDocumentBlockResponseBodyBuilder()


class PatchDocumentBlockResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_document_block_response_body = PatchDocumentBlockResponseBody()

    def block(self, block: Block) -> "PatchDocumentBlockResponseBodyBuilder":
        self._patch_document_block_response_body.block = block
        return self

    def document_revision_id(self, document_revision_id: int) -> "PatchDocumentBlockResponseBodyBuilder":
        self._patch_document_block_response_body.document_revision_id = document_revision_id
        return self

    def client_token(self, client_token: str) -> "PatchDocumentBlockResponseBodyBuilder":
        self._patch_document_block_response_body.client_token = client_token
        return self

    def build(self) -> "PatchDocumentBlockResponseBody":
        return self._patch_document_block_response_body