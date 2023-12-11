# Code generated by Lark OpenAPI.

import io
from typing import Optional

from requests_toolbelt import MultipartEncoder

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.download_file_request import DownloadFileRequest
from ..model.download_file_response import DownloadFileResponse
from ..model.upload_file_request import UploadFileRequest
from ..model.upload_file_response import UploadFileResponse


class File(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def download(self, request: DownloadFileRequest, option: Optional[RequestOption] = None) -> DownloadFileResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        content_type = resp.headers.get(CONTENT_TYPE)
        response: DownloadFileResponse = DownloadFileResponse()
        if 200 <= resp.status_code < 300:
            response.code = 0
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(resp.headers)
        elif content_type is not None and content_type.startswith(APPLICATION_JSON):
            response = JSON.unmarshal(str(resp.content, UTF_8), DownloadFileResponse)

        response.raw = resp
        return response

    def upload(self, request: UploadFileRequest, option: Optional[RequestOption] = None) -> UploadFileResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            request.body = form_data
            option.headers[CONTENT_TYPE] = form_data.content_type

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UploadFileResponse = JSON.unmarshal(str(resp.content, UTF_8), UploadFileResponse)
        response.raw = resp

        return response