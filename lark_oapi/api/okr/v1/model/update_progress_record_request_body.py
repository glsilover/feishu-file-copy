# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .content_block import ContentBlock


class UpdateProgressRecordRequestBody(object):
    _types = {
        "content": ContentBlock,
    }

    def __init__(self, d=None):
        self.content: Optional[ContentBlock] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProgressRecordRequestBodyBuilder":
        return UpdateProgressRecordRequestBodyBuilder()


class UpdateProgressRecordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._update_progress_record_request_body = UpdateProgressRecordRequestBody()

    def content(self, content: ContentBlock) -> "UpdateProgressRecordRequestBodyBuilder":
        self._update_progress_record_request_body.content = content
        return self

    def build(self) -> "UpdateProgressRecordRequestBody":
        return self._update_progress_record_request_body