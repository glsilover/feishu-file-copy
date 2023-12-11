# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateRoomRequest = CreateRoomRequest.builder() \
        .user_id_type("open_id") \
        .request_body(Room.builder()
                      .name("测试会议室")
                      .capacity(10)
                      .description("测试会议室描述")
                      .custom_room_id("1234")
                      .room_level_id("omb_8d020b12fe49e82847c2af3c193d5754")
                      .room_status(RoomStatus.builder().build())
                      .device([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateRoomResponse = client.vc.v1.room.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.room.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
