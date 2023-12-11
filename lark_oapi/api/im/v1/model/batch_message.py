# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .batch_recall_progress import BatchRecallProgress
from .batch_send_progress import BatchSendProgress


class BatchMessage(object):
    _types = {
        "batch_message_id": str,
        "batch_send_progress": BatchSendProgress,
        "batch_recall_progress": BatchRecallProgress,
    }

    def __init__(self, d=None):
        self.batch_message_id: Optional[str] = None
        self.batch_send_progress: Optional[BatchSendProgress] = None
        self.batch_recall_progress: Optional[BatchRecallProgress] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchMessageBuilder":
        return BatchMessageBuilder()


class BatchMessageBuilder(object):
    def __init__(self) -> None:
        self._batch_message = BatchMessage()

    def batch_message_id(self, batch_message_id: str) -> "BatchMessageBuilder":
        self._batch_message.batch_message_id = batch_message_id
        return self

    def batch_send_progress(self, batch_send_progress: BatchSendProgress) -> "BatchMessageBuilder":
        self._batch_message.batch_send_progress = batch_send_progress
        return self

    def batch_recall_progress(self, batch_recall_progress: BatchRecallProgress) -> "BatchMessageBuilder":
        self._batch_message.batch_recall_progress = batch_recall_progress
        return self

    def build(self) -> "BatchMessage":
        return self._batch_message
