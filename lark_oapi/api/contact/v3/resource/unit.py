# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.bind_department_unit_request import BindDepartmentUnitRequest
from ..model.bind_department_unit_response import BindDepartmentUnitResponse
from ..model.create_unit_request import CreateUnitRequest
from ..model.create_unit_response import CreateUnitResponse
from ..model.delete_unit_request import DeleteUnitRequest
from ..model.delete_unit_response import DeleteUnitResponse
from ..model.get_unit_request import GetUnitRequest
from ..model.get_unit_response import GetUnitResponse
from ..model.list_department_unit_request import ListDepartmentUnitRequest
from ..model.list_department_unit_response import ListDepartmentUnitResponse
from ..model.list_unit_request import ListUnitRequest
from ..model.list_unit_response import ListUnitResponse
from ..model.patch_unit_request import PatchUnitRequest
from ..model.patch_unit_response import PatchUnitResponse
from ..model.unbind_department_unit_request import UnbindDepartmentUnitRequest
from ..model.unbind_department_unit_response import UnbindDepartmentUnitResponse


class Unit(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def bind_department(self, request: BindDepartmentUnitRequest,
                        option: Optional[RequestOption] = None) -> BindDepartmentUnitResponse:
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
        response: BindDepartmentUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), BindDepartmentUnitResponse)
        response.raw = resp

        return response

    def create(self, request: CreateUnitRequest, option: Optional[RequestOption] = None) -> CreateUnitResponse:
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
        response: CreateUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateUnitResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteUnitRequest, option: Optional[RequestOption] = None) -> DeleteUnitResponse:
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
        response: DeleteUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteUnitResponse)
        response.raw = resp

        return response

    def get(self, request: GetUnitRequest, option: Optional[RequestOption] = None) -> GetUnitResponse:
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
        response: GetUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUnitResponse)
        response.raw = resp

        return response

    def list(self, request: ListUnitRequest, option: Optional[RequestOption] = None) -> ListUnitResponse:
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
        response: ListUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), ListUnitResponse)
        response.raw = resp

        return response

    def list_department(self, request: ListDepartmentUnitRequest,
                        option: Optional[RequestOption] = None) -> ListDepartmentUnitResponse:
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
        response: ListDepartmentUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), ListDepartmentUnitResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchUnitRequest, option: Optional[RequestOption] = None) -> PatchUnitResponse:
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
        response: PatchUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchUnitResponse)
        response.raw = resp

        return response

    def unbind_department(self, request: UnbindDepartmentUnitRequest,
                          option: Optional[RequestOption] = None) -> UnbindDepartmentUnitResponse:
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
        response: UnbindDepartmentUnitResponse = JSON.unmarshal(str(resp.content, UTF_8), UnbindDepartmentUnitResponse)
        response.raw = resp

        return response