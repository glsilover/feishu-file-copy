# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.helpdesk.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateAgentScheduleRequest = CreateAgentScheduleRequest.builder() \
        .request_body(CreateAgentScheduleRequestBody.builder()
                      .agent_schedules([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateAgentScheduleResponse = client.helpdesk.v1.agent_schedule.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.helpdesk.v1.agent_schedule.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
