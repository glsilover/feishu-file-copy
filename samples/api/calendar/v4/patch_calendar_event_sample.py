# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchCalendarEventRequest = PatchCalendarEventRequest.builder() \
        .calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
        .event_id("00592a0e-7edf-4678-bc9d-1b77383ef08e_0") \
        .user_id_type("user_id") \
        .request_body(CalendarEvent.builder()
                      .summary("日程标题")
                      .description("日程描述")
                      .need_notification(False)
                      .start_time(TimeInfo.builder().build())
                      .end_time(TimeInfo.builder().build())
                      .vchat(Vchat.builder().build())
                      .visibility("default")
                      .attendee_ability("none")
                      .free_busy_status("busy")
                      .location(EventLocation.builder().build())
                      .color(0)
                      .reminders([])
                      .recurrence("FREQ=DAILY;INTERVAL=1")
                      .schemas([])
                      .build()) \
        .build()

    # 发起请求
    response: PatchCalendarEventResponse = client.calendar.v4.calendar_event.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.calendar_event.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
