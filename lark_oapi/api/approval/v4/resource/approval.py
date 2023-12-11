# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_approval_request import CreateApprovalRequest
from ..model.create_approval_response import CreateApprovalResponse
from ..model.get_approval_request import GetApprovalRequest
from ..model.get_approval_response import GetApprovalResponse
from ..model.subscribe_approval_request import SubscribeApprovalRequest
from ..model.subscribe_approval_response import SubscribeApprovalResponse
from ..model.unsubscribe_approval_request import UnsubscribeApprovalRequest
from ..model.unsubscribe_approval_response import UnsubscribeApprovalResponse


class Approval(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateApprovalRequest, option: Optional[RequestOption] = None) -> CreateApprovalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateApprovalResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateApprovalResponse)
        response.raw = resp

        return response

    def get(self, request: GetApprovalRequest, option: Optional[RequestOption] = None) -> GetApprovalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetApprovalResponse = JSON.unmarshal(str(resp.content, UTF_8), GetApprovalResponse)
        response.raw = resp

        return response

    def subscribe(self, request: SubscribeApprovalRequest,
                  option: Optional[RequestOption] = None) -> SubscribeApprovalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SubscribeApprovalResponse = JSON.unmarshal(str(resp.content, UTF_8), SubscribeApprovalResponse)
        response.raw = resp

        return response

    def unsubscribe(self, request: UnsubscribeApprovalRequest,
                    option: Optional[RequestOption] = None) -> UnsubscribeApprovalResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UnsubscribeApprovalResponse = JSON.unmarshal(str(resp.content, UTF_8), UnsubscribeApprovalResponse)
        response.raw = resp

        return response