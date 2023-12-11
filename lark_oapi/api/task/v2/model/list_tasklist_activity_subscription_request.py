# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListTasklistActivitySubscriptionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.limit: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.tasklist_guid: Optional[str] = None

    @staticmethod
    def builder() -> "ListTasklistActivitySubscriptionRequestBuilder":
        return ListTasklistActivitySubscriptionRequestBuilder()


class ListTasklistActivitySubscriptionRequestBuilder(object):

    def __init__(self) -> None:
        list_tasklist_activity_subscription_request = ListTasklistActivitySubscriptionRequest()
        list_tasklist_activity_subscription_request.http_method = HttpMethod.GET
        list_tasklist_activity_subscription_request.uri = "/open-apis/task/v2/tasklists/:tasklist_guid/activity_subscriptions"
        list_tasklist_activity_subscription_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_tasklist_activity_subscription_request: ListTasklistActivitySubscriptionRequest = list_tasklist_activity_subscription_request

    def limit(self, limit: int) -> "ListTasklistActivitySubscriptionRequestBuilder":
        self._list_tasklist_activity_subscription_request.limit = limit
        self._list_tasklist_activity_subscription_request.add_query("limit", limit)
        return self

    def user_id_type(self, user_id_type: str) -> "ListTasklistActivitySubscriptionRequestBuilder":
        self._list_tasklist_activity_subscription_request.user_id_type = user_id_type
        self._list_tasklist_activity_subscription_request.add_query("user_id_type", user_id_type)
        return self

    def tasklist_guid(self, tasklist_guid: str) -> "ListTasklistActivitySubscriptionRequestBuilder":
        self._list_tasklist_activity_subscription_request.tasklist_guid = tasklist_guid
        self._list_tasklist_activity_subscription_request.paths["tasklist_guid"] = str(tasklist_guid)
        return self

    def build(self) -> ListTasklistActivitySubscriptionRequest:
        return self._list_tasklist_activity_subscription_request
