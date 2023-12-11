# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_company_request import CreateCompanyRequest
from ..model.create_company_response import CreateCompanyResponse
from ..model.delete_company_request import DeleteCompanyRequest
from ..model.delete_company_response import DeleteCompanyResponse
from ..model.get_company_request import GetCompanyRequest
from ..model.get_company_response import GetCompanyResponse
from ..model.list_company_request import ListCompanyRequest
from ..model.list_company_response import ListCompanyResponse


class Company(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateCompanyRequest, option: Optional[RequestOption] = None) -> CreateCompanyResponse:
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
        response: CreateCompanyResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateCompanyResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteCompanyRequest, option: Optional[RequestOption] = None) -> DeleteCompanyResponse:
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
        response: DeleteCompanyResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteCompanyResponse)
        response.raw = resp

        return response

    def get(self, request: GetCompanyRequest, option: Optional[RequestOption] = None) -> GetCompanyResponse:
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
        response: GetCompanyResponse = JSON.unmarshal(str(resp.content, UTF_8), GetCompanyResponse)
        response.raw = resp

        return response

    def list(self, request: ListCompanyRequest, option: Optional[RequestOption] = None) -> ListCompanyResponse:
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
        response: ListCompanyResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCompanyResponse)
        response.raw = resp

        return response