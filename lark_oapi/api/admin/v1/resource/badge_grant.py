# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_badge_grant_request import CreateBadgeGrantRequest
from ..model.create_badge_grant_response import CreateBadgeGrantResponse
from ..model.delete_badge_grant_request import DeleteBadgeGrantRequest
from ..model.delete_badge_grant_response import DeleteBadgeGrantResponse
from ..model.get_badge_grant_request import GetBadgeGrantRequest
from ..model.get_badge_grant_response import GetBadgeGrantResponse
from ..model.list_badge_grant_request import ListBadgeGrantRequest
from ..model.list_badge_grant_response import ListBadgeGrantResponse
from ..model.update_badge_grant_request import UpdateBadgeGrantRequest
from ..model.update_badge_grant_response import UpdateBadgeGrantResponse


class BadgeGrant(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateBadgeGrantRequest,
               option: Optional[RequestOption] = None) -> CreateBadgeGrantResponse:
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
        response: CreateBadgeGrantResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateBadgeGrantResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteBadgeGrantRequest,
               option: Optional[RequestOption] = None) -> DeleteBadgeGrantResponse:
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
        response: DeleteBadgeGrantResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteBadgeGrantResponse)
        response.raw = resp

        return response

    def get(self, request: GetBadgeGrantRequest, option: Optional[RequestOption] = None) -> GetBadgeGrantResponse:
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
        response: GetBadgeGrantResponse = JSON.unmarshal(str(resp.content, UTF_8), GetBadgeGrantResponse)
        response.raw = resp

        return response

    def list(self, request: ListBadgeGrantRequest, option: Optional[RequestOption] = None) -> ListBadgeGrantResponse:
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
        response: ListBadgeGrantResponse = JSON.unmarshal(str(resp.content, UTF_8), ListBadgeGrantResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateBadgeGrantRequest,
               option: Optional[RequestOption] = None) -> UpdateBadgeGrantResponse:
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
        response: UpdateBadgeGrantResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateBadgeGrantResponse)
        response.raw = resp

        return response
