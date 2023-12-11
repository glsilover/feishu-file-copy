# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.locale: Optional[str] = None
        self.user_id: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.instance_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetInstanceRequestBuilder":
        return GetInstanceRequestBuilder()


class GetInstanceRequestBuilder(object):

    def __init__(self) -> None:
        get_instance_request = GetInstanceRequest()
        get_instance_request.http_method = HttpMethod.GET
        get_instance_request.uri = "/open-apis/approval/v4/instances/:instance_id"
        get_instance_request.token_types = {AccessTokenType.TENANT}
        self._get_instance_request: GetInstanceRequest = get_instance_request

    def locale(self, locale: str) -> "GetInstanceRequestBuilder":
        self._get_instance_request.locale = locale
        self._get_instance_request.add_query("locale", locale)
        return self

    def user_id(self, user_id: str) -> "GetInstanceRequestBuilder":
        self._get_instance_request.user_id = user_id
        self._get_instance_request.add_query("user_id", user_id)
        return self

    def user_id_type(self, user_id_type: str) -> "GetInstanceRequestBuilder":
        self._get_instance_request.user_id_type = user_id_type
        self._get_instance_request.add_query("user_id_type", user_id_type)
        return self

    def instance_id(self, instance_id: str) -> "GetInstanceRequestBuilder":
        self._get_instance_request.instance_id = instance_id
        self._get_instance_request.paths["instance_id"] = str(instance_id)
        return self

    def build(self) -> GetInstanceRequest:
        return self._get_instance_request
