# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class FaqUpdateInfo(object):
    _types = {
        "category_id": str,
        "question": str,
        "answer": str,
        "answer_richtext": str,
        "tags": List[str],
    }

    def __init__(self, d=None):
        self.category_id: Optional[str] = None
        self.question: Optional[str] = None
        self.answer: Optional[str] = None
        self.answer_richtext: Optional[str] = None
        self.tags: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FaqUpdateInfoBuilder":
        return FaqUpdateInfoBuilder()


class FaqUpdateInfoBuilder(object):
    def __init__(self) -> None:
        self._faq_update_info = FaqUpdateInfo()

    def category_id(self, category_id: str) -> "FaqUpdateInfoBuilder":
        self._faq_update_info.category_id = category_id
        return self

    def question(self, question: str) -> "FaqUpdateInfoBuilder":
        self._faq_update_info.question = question
        return self

    def answer(self, answer: str) -> "FaqUpdateInfoBuilder":
        self._faq_update_info.answer = answer
        return self

    def answer_richtext(self, answer_richtext: str) -> "FaqUpdateInfoBuilder":
        self._faq_update_info.answer_richtext = answer_richtext
        return self

    def tags(self, tags: List[str]) -> "FaqUpdateInfoBuilder":
        self._faq_update_info.tags = tags
        return self

    def build(self) -> "FaqUpdateInfo":
        return self._faq_update_info
