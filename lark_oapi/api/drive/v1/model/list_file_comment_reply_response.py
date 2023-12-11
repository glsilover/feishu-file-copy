# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_file_comment_reply_response_body import ListFileCommentReplyResponseBody


class ListFileCommentReplyResponse(BaseResponse):
    _types = {
        "data": ListFileCommentReplyResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListFileCommentReplyResponseBody] = None
        init(self, d, self._types)
