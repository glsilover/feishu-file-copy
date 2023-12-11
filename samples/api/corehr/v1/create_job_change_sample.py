# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateJobChangeRequest = CreateJobChangeRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("people_corehr_department_id") \
        .request_body(CreateJobChangeRequestBody.builder()
                      .transfer_mode(2)
                      .employment_id("ou_a294793e8fa21529f2a60e3e9de45520")
                      .transfer_type_unique_identifier("internal_transfer")
                      .flow_id("people_6963913041981490725_6983885526583627531")
                      .effective_date("2022-03-01")
                      .transfer_info(TransferInfo.builder().build())
                      .transfer_key("transfer_3627531")
                      .initiator_id("ou_a294793e8fa21529f2a60e3e9de45520")
                      .build()) \
        .build()

    # 发起请求
    response: CreateJobChangeResponse = client.corehr.v1.job_change.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.job_change.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
