# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .okr_review_period_url import OkrReviewPeriodUrl


class OkrReviewPeriod(object):
    _types = {
        "period_id": int,
        "cycle_review_list": List[OkrReviewPeriodUrl],
        "progress_report_list": List[OkrReviewPeriodUrl],
    }

    def __init__(self, d=None):
        self.period_id: Optional[int] = None
        self.cycle_review_list: Optional[List[OkrReviewPeriodUrl]] = None
        self.progress_report_list: Optional[List[OkrReviewPeriodUrl]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrReviewPeriodBuilder":
        return OkrReviewPeriodBuilder()


class OkrReviewPeriodBuilder(object):
    def __init__(self) -> None:
        self._okr_review_period = OkrReviewPeriod()

    def period_id(self, period_id: int) -> "OkrReviewPeriodBuilder":
        self._okr_review_period.period_id = period_id
        return self

    def cycle_review_list(self, cycle_review_list: List[OkrReviewPeriodUrl]) -> "OkrReviewPeriodBuilder":
        self._okr_review_period.cycle_review_list = cycle_review_list
        return self

    def progress_report_list(self, progress_report_list: List[OkrReviewPeriodUrl]) -> "OkrReviewPeriodBuilder":
        self._okr_review_period.progress_report_list = progress_report_list
        return self

    def build(self) -> "OkrReviewPeriod":
        return self._okr_review_period