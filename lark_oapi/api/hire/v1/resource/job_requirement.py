# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_job_requirement_request import CreateJobRequirementRequest
from ..model.create_job_requirement_response import CreateJobRequirementResponse
from ..model.delete_job_requirement_request import DeleteJobRequirementRequest
from ..model.delete_job_requirement_response import DeleteJobRequirementResponse
from ..model.list_by_id_job_requirement_request import ListByIdJobRequirementRequest
from ..model.list_by_id_job_requirement_response import ListByIdJobRequirementResponse
from ..model.list_job_requirement_request import ListJobRequirementRequest
from ..model.list_job_requirement_response import ListJobRequirementResponse
from ..model.update_job_requirement_request import UpdateJobRequirementRequest
from ..model.update_job_requirement_response import UpdateJobRequirementResponse


class JobRequirement(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateJobRequirementRequest,
               option: Optional[RequestOption] = None) -> CreateJobRequirementResponse:
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
        response: CreateJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobRequirementResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobRequirementRequest,
               option: Optional[RequestOption] = None) -> DeleteJobRequirementResponse:
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
        response: DeleteJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobRequirementResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobRequirementRequest,
             option: Optional[RequestOption] = None) -> ListJobRequirementResponse:
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
        response: ListJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobRequirementResponse)
        response.raw = resp

        return response

    def list_by_id(self, request: ListByIdJobRequirementRequest,
                   option: Optional[RequestOption] = None) -> ListByIdJobRequirementResponse:
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
        response: ListByIdJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                  ListByIdJobRequirementResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateJobRequirementRequest,
               option: Optional[RequestOption] = None) -> UpdateJobRequirementResponse:
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
        response: UpdateJobRequirementResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateJobRequirementResponse)
        response.raw = resp

        return response