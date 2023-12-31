# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_delete_eco_exam_paper_request import BatchDeleteEcoExamPaperRequest
from ..model.batch_delete_eco_exam_paper_response import BatchDeleteEcoExamPaperResponse
from ..model.batch_update_eco_exam_paper_request import BatchUpdateEcoExamPaperRequest
from ..model.batch_update_eco_exam_paper_response import BatchUpdateEcoExamPaperResponse
from ..model.create_eco_exam_paper_request import CreateEcoExamPaperRequest
from ..model.create_eco_exam_paper_response import CreateEcoExamPaperResponse


class EcoExamPaper(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_delete(self, request: BatchDeleteEcoExamPaperRequest,
                     option: Optional[RequestOption] = None) -> BatchDeleteEcoExamPaperResponse:
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
        response: BatchDeleteEcoExamPaperResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   BatchDeleteEcoExamPaperResponse)
        response.raw = resp

        return response

    def batch_update(self, request: BatchUpdateEcoExamPaperRequest,
                     option: Optional[RequestOption] = None) -> BatchUpdateEcoExamPaperResponse:
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
        response: BatchUpdateEcoExamPaperResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   BatchUpdateEcoExamPaperResponse)
        response.raw = resp

        return response

    def create(self, request: CreateEcoExamPaperRequest,
               option: Optional[RequestOption] = None) -> CreateEcoExamPaperResponse:
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
        response: CreateEcoExamPaperResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateEcoExamPaperResponse)
        response.raw = resp

        return response
