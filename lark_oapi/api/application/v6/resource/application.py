# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.contacts_range_configuration_application_request import ContactsRangeConfigurationApplicationRequest
from ..model.contacts_range_configuration_application_response import ContactsRangeConfigurationApplicationResponse
from ..model.get_application_request import GetApplicationRequest
from ..model.get_application_response import GetApplicationResponse
from ..model.patch_application_request import PatchApplicationRequest
from ..model.patch_application_response import PatchApplicationResponse
from ..model.underauditlist_application_request import UnderauditlistApplicationRequest
from ..model.underauditlist_application_response import UnderauditlistApplicationResponse


class Application(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def contacts_range_configuration(self, request: ContactsRangeConfigurationApplicationRequest, option: Optional[
        RequestOption] = None) -> ContactsRangeConfigurationApplicationResponse:
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
        response: ContactsRangeConfigurationApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                 ContactsRangeConfigurationApplicationResponse)
        response.raw = resp

        return response

    def get(self, request: GetApplicationRequest, option: Optional[RequestOption] = None) -> GetApplicationResponse:
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
        response: GetApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), GetApplicationResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchApplicationRequest,
              option: Optional[RequestOption] = None) -> PatchApplicationResponse:
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
        response: PatchApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchApplicationResponse)
        response.raw = resp

        return response

    def underauditlist(self, request: UnderauditlistApplicationRequest,
                       option: Optional[RequestOption] = None) -> UnderauditlistApplicationResponse:
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
        response: UnderauditlistApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     UnderauditlistApplicationResponse)
        response.raw = resp

        return response
