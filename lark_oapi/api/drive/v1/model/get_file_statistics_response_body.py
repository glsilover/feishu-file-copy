# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .file_statistics import FileStatistics


class GetFileStatisticsResponseBody(object):
    _types = {
        "file_token": str,
        "file_type": str,
        "statistics": FileStatistics,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.file_type: Optional[str] = None
        self.statistics: Optional[FileStatistics] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetFileStatisticsResponseBodyBuilder":
        return GetFileStatisticsResponseBodyBuilder()


class GetFileStatisticsResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_file_statistics_response_body = GetFileStatisticsResponseBody()

    def file_token(self, file_token: str) -> "GetFileStatisticsResponseBodyBuilder":
        self._get_file_statistics_response_body.file_token = file_token
        return self

    def file_type(self, file_type: str) -> "GetFileStatisticsResponseBodyBuilder":
        self._get_file_statistics_response_body.file_type = file_type
        return self

    def statistics(self, statistics: FileStatistics) -> "GetFileStatisticsResponseBodyBuilder":
        self._get_file_statistics_response_body.statistics = statistics
        return self

    def build(self) -> "GetFileStatisticsResponseBody":
        return self._get_file_statistics_response_body
