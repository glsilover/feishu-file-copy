# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .data_archiving_user_struct import DataArchivingUserStruct


class DataArchivingMessageStruct(object):
    _types = {
        "message_id": str,
        "message_type": int,
        "sender_info": DataArchivingUserStruct,
        "receiver_ids": List[str],
        "action_type": str,
        "chat_id": int,
        "action_time": int,
        "is_super_chat": bool,
        "is_cross_tenant_chat": bool,
        "chat_name": str,
        "content": str,
        "chat_mode": str,
        "reaction_type": str,
        "parent_msg_id": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.message_type: Optional[int] = None
        self.sender_info: Optional[DataArchivingUserStruct] = None
        self.receiver_ids: Optional[List[str]] = None
        self.action_type: Optional[str] = None
        self.chat_id: Optional[int] = None
        self.action_time: Optional[int] = None
        self.is_super_chat: Optional[bool] = None
        self.is_cross_tenant_chat: Optional[bool] = None
        self.chat_name: Optional[str] = None
        self.content: Optional[str] = None
        self.chat_mode: Optional[str] = None
        self.reaction_type: Optional[str] = None
        self.parent_msg_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DataArchivingMessageStructBuilder":
        return DataArchivingMessageStructBuilder()


class DataArchivingMessageStructBuilder(object):
    def __init__(self) -> None:
        self._data_archiving_message_struct = DataArchivingMessageStruct()

    def message_id(self, message_id: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.message_id = message_id
        return self

    def message_type(self, message_type: int) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.message_type = message_type
        return self

    def sender_info(self, sender_info: DataArchivingUserStruct) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.sender_info = sender_info
        return self

    def receiver_ids(self, receiver_ids: List[str]) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.receiver_ids = receiver_ids
        return self

    def action_type(self, action_type: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.action_type = action_type
        return self

    def chat_id(self, chat_id: int) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.chat_id = chat_id
        return self

    def action_time(self, action_time: int) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.action_time = action_time
        return self

    def is_super_chat(self, is_super_chat: bool) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.is_super_chat = is_super_chat
        return self

    def is_cross_tenant_chat(self, is_cross_tenant_chat: bool) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.is_cross_tenant_chat = is_cross_tenant_chat
        return self

    def chat_name(self, chat_name: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.chat_name = chat_name
        return self

    def content(self, content: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.content = content
        return self

    def chat_mode(self, chat_mode: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.chat_mode = chat_mode
        return self

    def reaction_type(self, reaction_type: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.reaction_type = reaction_type
        return self

    def parent_msg_id(self, parent_msg_id: str) -> "DataArchivingMessageStructBuilder":
        self._data_archiving_message_struct.parent_msg_id = parent_msg_id
        return self

    def build(self) -> "DataArchivingMessageStruct":
        return self._data_archiving_message_struct
