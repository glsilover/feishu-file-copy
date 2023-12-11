# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class InterviewScore(object):
    _types = {
        "id": str,
        "level": int,
        "zh_name": str,
        "zh_description": str,
        "en_name": str,
        "en_description": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.level: Optional[int] = None
        self.zh_name: Optional[str] = None
        self.zh_description: Optional[str] = None
        self.en_name: Optional[str] = None
        self.en_description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewScoreBuilder":
        return InterviewScoreBuilder()


class InterviewScoreBuilder(object):
    def __init__(self) -> None:
        self._interview_score = InterviewScore()

    def id(self, id: str) -> "InterviewScoreBuilder":
        self._interview_score.id = id
        return self

    def level(self, level: int) -> "InterviewScoreBuilder":
        self._interview_score.level = level
        return self

    def zh_name(self, zh_name: str) -> "InterviewScoreBuilder":
        self._interview_score.zh_name = zh_name
        return self

    def zh_description(self, zh_description: str) -> "InterviewScoreBuilder":
        self._interview_score.zh_description = zh_description
        return self

    def en_name(self, en_name: str) -> "InterviewScoreBuilder":
        self._interview_score.en_name = en_name
        return self

    def en_description(self, en_description: str) -> "InterviewScoreBuilder":
        self._interview_score.en_description = en_description
        return self

    def build(self) -> "InterviewScore":
        return self._interview_score
