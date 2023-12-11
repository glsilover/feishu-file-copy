# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class WebPassageParam(object):
    _types = {
        "searchable": bool,
        "domains": List[str],
    }

    def __init__(self, d=None):
        self.searchable: Optional[bool] = None
        self.domains: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebPassageParamBuilder":
        return WebPassageParamBuilder()


class WebPassageParamBuilder(object):
    def __init__(self) -> None:
        self._web_passage_param = WebPassageParam()

    def searchable(self, searchable: bool) -> "WebPassageParamBuilder":
        self._web_passage_param.searchable = searchable
        return self

    def domains(self, domains: List[str]) -> "WebPassageParamBuilder":
        self._web_passage_param.domains = domains
        return self

    def build(self) -> "WebPassageParam":
        return self._web_passage_param