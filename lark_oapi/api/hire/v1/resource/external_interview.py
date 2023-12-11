# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_external_interview_request import CreateExternalInterviewRequest
from ..model.create_external_interview_response import CreateExternalInterviewResponse


class ExternalInterview(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateExternalInterviewRequest,
               option: Optional[RequestOption] = None) -> CreateExternalInterviewResponse:
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
        response: CreateExternalInterviewResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   CreateExternalInterviewResponse)
        response.raw = resp

        return response