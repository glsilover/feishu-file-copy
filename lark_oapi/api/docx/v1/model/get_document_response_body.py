# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .document import Document


class GetDocumentResponseBody(object):
    _types = {
        "document": Document,
    }

    def __init__(self, d=None):
        self.document: Optional[Document] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetDocumentResponseBodyBuilder":
        return GetDocumentResponseBodyBuilder()


class GetDocumentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_document_response_body = GetDocumentResponseBody()

    def document(self, document: Document) -> "GetDocumentResponseBodyBuilder":
        self._get_document_response_body.document = document
        return self

    def build(self) -> "GetDocumentResponseBody":
        return self._get_document_response_body