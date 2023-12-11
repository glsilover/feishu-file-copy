# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.file_recognize_speech_request import FileRecognizeSpeechRequest
from ..model.file_recognize_speech_response import FileRecognizeSpeechResponse
from ..model.stream_recognize_speech_request import StreamRecognizeSpeechRequest
from ..model.stream_recognize_speech_response import StreamRecognizeSpeechResponse


class Speech(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def file_recognize(self, request: FileRecognizeSpeechRequest,
                       option: Optional[RequestOption] = None) -> FileRecognizeSpeechResponse:
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
        response: FileRecognizeSpeechResponse = JSON.unmarshal(str(resp.content, UTF_8), FileRecognizeSpeechResponse)
        response.raw = resp

        return response

    def stream_recognize(self, request: StreamRecognizeSpeechRequest,
                         option: Optional[RequestOption] = None) -> StreamRecognizeSpeechResponse:
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
        response: StreamRecognizeSpeechResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 StreamRecognizeSpeechResponse)
        response.raw = resp

        return response
