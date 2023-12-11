# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .text_element import TextElement


class UpdateTextElementsRequest(object):
    _types = {
        "elements": List[TextElement],
    }

    def __init__(self, d=None):
        self.elements: Optional[List[TextElement]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTextElementsRequestBuilder":
        return UpdateTextElementsRequestBuilder()


class UpdateTextElementsRequestBuilder(object):
    def __init__(self) -> None:
        self._update_text_elements_request = UpdateTextElementsRequest()

    def elements(self, elements: List[TextElement]) -> "UpdateTextElementsRequestBuilder":
        self._update_text_elements_request.elements = elements
        return self

    def build(self) -> "UpdateTextElementsRequest":
        return self._update_text_elements_request