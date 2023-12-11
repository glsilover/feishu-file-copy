# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class FileUploadInfo(object):
    _types = {
        "file_name": str,
        "parent_type": str,
        "parent_node": str,
        "size": int,
    }

    def __init__(self, d=None):
        self.file_name: Optional[str] = None
        self.parent_type: Optional[str] = None
        self.parent_node: Optional[str] = None
        self.size: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileUploadInfoBuilder":
        return FileUploadInfoBuilder()


class FileUploadInfoBuilder(object):
    def __init__(self) -> None:
        self._file_upload_info = FileUploadInfo()

    def file_name(self, file_name: str) -> "FileUploadInfoBuilder":
        self._file_upload_info.file_name = file_name
        return self

    def parent_type(self, parent_type: str) -> "FileUploadInfoBuilder":
        self._file_upload_info.parent_type = parent_type
        return self

    def parent_node(self, parent_node: str) -> "FileUploadInfoBuilder":
        self._file_upload_info.parent_node = parent_node
        return self

    def size(self, size: int) -> "FileUploadInfoBuilder":
        self._file_upload_info.size = size
        return self

    def build(self) -> "FileUploadInfo":
        return self._file_upload_info
