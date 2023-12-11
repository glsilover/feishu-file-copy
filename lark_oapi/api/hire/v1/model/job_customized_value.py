# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .job_customized_option import JobCustomizedOption
from .job_customized_time_range import JobCustomizedTimeRange


class JobCustomizedValue(object):
    _types = {
        "content": str,
        "option": JobCustomizedOption,
        "option_list": List[JobCustomizedOption],
        "time_range": JobCustomizedTimeRange,
        "time": str,
        "number": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.option: Optional[JobCustomizedOption] = None
        self.option_list: Optional[List[JobCustomizedOption]] = None
        self.time_range: Optional[JobCustomizedTimeRange] = None
        self.time: Optional[str] = None
        self.number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobCustomizedValueBuilder":
        return JobCustomizedValueBuilder()


class JobCustomizedValueBuilder(object):
    def __init__(self) -> None:
        self._job_customized_value = JobCustomizedValue()

    def content(self, content: str) -> "JobCustomizedValueBuilder":
        self._job_customized_value.content = content
        return self

    def option(self, option: JobCustomizedOption) -> "JobCustomizedValueBuilder":
        self._job_customized_value.option = option
        return self

    def option_list(self, option_list: List[JobCustomizedOption]) -> "JobCustomizedValueBuilder":
        self._job_customized_value.option_list = option_list
        return self

    def time_range(self, time_range: JobCustomizedTimeRange) -> "JobCustomizedValueBuilder":
        self._job_customized_value.time_range = time_range
        return self

    def time(self, time: str) -> "JobCustomizedValueBuilder":
        self._job_customized_value.time = time
        return self

    def number(self, number: str) -> "JobCustomizedValueBuilder":
        self._job_customized_value.number = number
        return self

    def build(self) -> "JobCustomizedValue":
        return self._job_customized_value
