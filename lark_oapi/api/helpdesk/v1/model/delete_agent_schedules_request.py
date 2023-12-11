# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteAgentSchedulesRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAgentSchedulesRequestBuilder":
        return DeleteAgentSchedulesRequestBuilder()


class DeleteAgentSchedulesRequestBuilder(object):

    def __init__(self) -> None:
        delete_agent_schedules_request = DeleteAgentSchedulesRequest()
        delete_agent_schedules_request.http_method = HttpMethod.DELETE
        delete_agent_schedules_request.uri = "/open-apis/helpdesk/v1/agents/:agent_id/schedules"
        delete_agent_schedules_request.token_types = {AccessTokenType.USER}
        self._delete_agent_schedules_request: DeleteAgentSchedulesRequest = delete_agent_schedules_request

    def agent_id(self, agent_id: str) -> "DeleteAgentSchedulesRequestBuilder":
        self._delete_agent_schedules_request.agent_id = agent_id
        self._delete_agent_schedules_request.paths["agent_id"] = str(agent_id)
        return self

    def build(self) -> DeleteAgentSchedulesRequest:
        return self._delete_agent_schedules_request