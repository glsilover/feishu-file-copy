# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.cancel_approve_notification_request import CancelApproveNotificationRequest
from ..model.cancel_approve_notification_response import CancelApproveNotificationResponse
from ..model.cancel_send_notification_request import CancelSendNotificationRequest
from ..model.cancel_send_notification_response import CancelSendNotificationResponse
from ..model.create_notification_request import CreateNotificationRequest
from ..model.create_notification_response import CreateNotificationResponse
from ..model.execute_send_notification_request import ExecuteSendNotificationRequest
from ..model.execute_send_notification_response import ExecuteSendNotificationResponse
from ..model.get_notification_request import GetNotificationRequest
from ..model.get_notification_response import GetNotificationResponse
from ..model.patch_notification_request import PatchNotificationRequest
from ..model.patch_notification_response import PatchNotificationResponse
from ..model.preview_notification_request import PreviewNotificationRequest
from ..model.preview_notification_response import PreviewNotificationResponse
from ..model.submit_approve_notification_request import SubmitApproveNotificationRequest
from ..model.submit_approve_notification_response import SubmitApproveNotificationResponse


class Notification(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def cancel_approve(self, request: CancelApproveNotificationRequest,
                       option: Optional[RequestOption] = None) -> CancelApproveNotificationResponse:
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
        response: CancelApproveNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     CancelApproveNotificationResponse)
        response.raw = resp

        return response

    def cancel_send(self, request: CancelSendNotificationRequest,
                    option: Optional[RequestOption] = None) -> CancelSendNotificationResponse:
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
        response: CancelSendNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  CancelSendNotificationResponse)
        response.raw = resp

        return response

    def create(self, request: CreateNotificationRequest,
               option: Optional[RequestOption] = None) -> CreateNotificationResponse:
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
        response: CreateNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateNotificationResponse)
        response.raw = resp

        return response

    def execute_send(self, request: ExecuteSendNotificationRequest,
                     option: Optional[RequestOption] = None) -> ExecuteSendNotificationResponse:
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
        response: ExecuteSendNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   ExecuteSendNotificationResponse)
        response.raw = resp

        return response

    def get(self, request: GetNotificationRequest, option: Optional[RequestOption] = None) -> GetNotificationResponse:
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
        response: GetNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8), GetNotificationResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchNotificationRequest,
              option: Optional[RequestOption] = None) -> PatchNotificationResponse:
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
        response: PatchNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchNotificationResponse)
        response.raw = resp

        return response

    def preview(self, request: PreviewNotificationRequest,
                option: Optional[RequestOption] = None) -> PreviewNotificationResponse:
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
        response: PreviewNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8), PreviewNotificationResponse)
        response.raw = resp

        return response

    def submit_approve(self, request: SubmitApproveNotificationRequest,
                       option: Optional[RequestOption] = None) -> SubmitApproveNotificationResponse:
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
        response: SubmitApproveNotificationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     SubmitApproveNotificationResponse)
        response.raw = resp

        return response
