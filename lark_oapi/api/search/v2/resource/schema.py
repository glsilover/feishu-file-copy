# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_schema_request import CreateSchemaRequest
from ..model.create_schema_response import CreateSchemaResponse
from ..model.delete_schema_request import DeleteSchemaRequest
from ..model.delete_schema_response import DeleteSchemaResponse
from ..model.get_schema_request import GetSchemaRequest
from ..model.get_schema_response import GetSchemaResponse
from ..model.patch_schema_request import PatchSchemaRequest
from ..model.patch_schema_response import PatchSchemaResponse


class Schema(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateSchemaRequest, option: Optional[RequestOption] = None) -> CreateSchemaResponse:
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
        response: CreateSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSchemaResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteSchemaRequest, option: Optional[RequestOption] = None) -> DeleteSchemaResponse:
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
        response: DeleteSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteSchemaResponse)
        response.raw = resp

        return response

    def get(self, request: GetSchemaRequest, option: Optional[RequestOption] = None) -> GetSchemaResponse:
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
        response: GetSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSchemaResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchSchemaRequest, option: Optional[RequestOption] = None) -> PatchSchemaResponse:
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
        response: PatchSchemaResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchSchemaResponse)
        response.raw = resp

        return response