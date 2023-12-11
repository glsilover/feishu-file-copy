# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.list_special_focus_request import ListSpecialFocusRequest
from ..model.list_special_focus_response import ListSpecialFocusResponse
from ..model.unread_special_focus_request import UnreadSpecialFocusRequest
from ..model.unread_special_focus_response import UnreadSpecialFocusResponse


class SpecialFocus(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list(self, request: ListSpecialFocusRequest,
             option: Optional[RequestOption] = None) -> ListSpecialFocusResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListSpecialFocusResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSpecialFocusResponse)
        response.raw = resp

        return response

    def unread(self, request: UnreadSpecialFocusRequest,
               option: Optional[RequestOption] = None) -> UnreadSpecialFocusResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UnreadSpecialFocusResponse = JSON.unmarshal(str(resp.content, UTF_8), UnreadSpecialFocusResponse)
        response.raw = resp

        return response