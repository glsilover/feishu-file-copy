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
    request: MatchCompensationStandardRequest = MatchCompensationStandardRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("people_corehr_department_id") \
        .employment_id("7124293751317038636") \
        .reference_object_api("cpst_item") \
        .reference_object_id("7156853394442044972") \
        .department_id("od-53899868dd0da32292a2d809f0518c8f") \
        .work_location_id("7094869485965870636") \
        .company_id("7091599096804394540") \
        .job_family_id("7039313681989502508") \
        .job_level_id("7086415175263258156") \
        .employee_type_id("7039310401359775276") \
        .recruitment_type("experienced_professionals") \
        .cpst_change_reason_id("6967639606963471117") \
        .cpst_plan_id("6967639606963471118") \
        .cpst_salary_level_id("6967639606963471119") \
        .effective_time("1660924800000") \
        .build()

    # 发起请求
    response: MatchCompensationStandardResponse = client.corehr.v1.compensation_standard.match(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.compensation_standard.match failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
