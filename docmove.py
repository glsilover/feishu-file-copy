import lark_oapi as lark
from lark_oapi.api.drive.v2 import *
from lark_oapi.api.drive.v1 import *
import json
import requests

# 个人账号
user_access_token_personal = 'XXX'

# 企业账号
user_access_token_ksyun = 'XXX'


# %%
# 获取根目录的文件夹元数据
def get_root_folder_meta(user_access_token):
    url = "https://open.feishu.cn/open-apis/drive/explorer/v2/root_folder/meta"

    payload = {}
    authorization_content = f"Bearer {user_access_token}"
    headers = {
        'Authorization': authorization_content,
        # 'Cookie': '_csrf_token=52e6770c8e9b3bb4ec9b4c7eec1d00b08dabab68-1702291538'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)


# 获取空间下所有文件list，包含文件夹、文件，注意文件夹不会递归查找文件
def get_file_list(user_access_token, folder_token=''):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.ERROR) \
        .build()

    # 构造请求对象
    request: ListFileRequest = ListFileRequest.builder() \
        .page_size(200) \
        .folder_token(folder_token) \
        .order_by("EditedTime") \
        .direction("DESC") \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: ListFileResponse = client.drive.v1.file.list(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    return json.loads(lark.JSON.marshal(response.data, indent=4))


# 创建新文件夹
def creat_folder(folder_name, parent_folder_token, user_access_token):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.ERROR) \
        .build()

    # 构造请求对象
    request: CreateFolderFileRequest = CreateFolderFileRequest.builder() \
        .request_body(CreateFolderFileRequestBody.builder()
                      .name(folder_name)
                      .folder_token(parent_folder_token)
                      .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: CreateFolderFileResponse = client.drive.v1.file.create_folder(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file.create_folder failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    return json.loads(lark.JSON.marshal(response.data, indent=4))


# 修改文件权限，使互联网所有人可编辑
from lark_oapi.api.drive.v2 import *


def modification_file_entity(file_token, file_type, user_access_token):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.ERROR) \
        .build()

    # 构造请求对象
    request: PatchPermissionPublicRequest = PatchPermissionPublicRequest.builder() \
        .token(file_token) \
        .type(file_type) \
        .request_body(PermissionPublic.builder()
                      .external_access_entity("open")
                      .security_entity("anyone_can_edit")
                      .comment_entity("anyone_can_view")
                      .share_entity("anyone")
                      .manage_collaborator_entity("collaborator_can_view")
                      .link_share_entity("anyone_editable")
                      .copy_entity("anyone_can_view")
                      .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: PatchPermissionPublicResponse = client.drive.v2.permission_public.patch(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v2.permission_public.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    print(response.code)
    return json.loads(lark.JSON.marshal(response.data, indent=4))


# 取消文件互联网访问权限为私密（仅自己和协作者可访问）
def modification_file_entity_rollback(file_token, file_type, user_access_token):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.ERROR) \
        .build()

    # 构造请求对象
    request: PatchPermissionPublicRequest = PatchPermissionPublicRequest.builder() \
        .token(file_token) \
        .type(file_type) \
        .request_body(PermissionPublic.builder()
                      .external_access_entity("closed")
                      .security_entity("only_full_access")
                      .comment_entity("anyone_can_view")
                      .share_entity("same_tenant")
                      .manage_collaborator_entity("collaborator_can_view")
                      .link_share_entity("tenant_readable")
                      .copy_entity("only_full_access")
                      .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: PatchPermissionPublicResponse = client.drive.v2.permission_public.patch(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v2.permission_public.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    print(response.code)
    return json.loads(lark.JSON.marshal(response.data, indent=4))


# 根据已有文件token，copy文件至指定目录下。
def copy_file(file_token, file_name, file_type, folder_token, user_access_token):
    # 创建client
    # 使用 user_access_token 需开启 token 配置, 并在 request_option 中配置 token
    client = lark.Client.builder() \
        .enable_set_token(True) \
        .log_level(lark.LogLevel.ERROR) \
        .build()

    # 构造请求对象
    request: CopyFileRequest = CopyFileRequest.builder() \
        .file_token(file_token) \
        .request_body(CopyFileRequestBody.builder()
                      .name(file_name)
                      .type(file_type)
                      .folder_token(folder_token)
                      .build()) \
        .build()

    # 发起请求
    option = lark.RequestOption.builder().user_access_token(user_access_token).build()
    response: CopyFileResponse = client.drive.v1.file.copy(request, option)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file.copy failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))
    return json.loads(lark.JSON.marshal(response.data, indent=4))


# 递归获取金山云所有文件夹和文件，并在个人账号创建相同的文件夹和文件
def main(folder_token):

    def recurse_folder(token):
        try:
            for item in get_file_list(user_access_token_ksyun, token)['files']:
                if item['type'] == 'folder':
                    # 每chazhaoyige
                    new_folder = creat_folder(item['name'], folder_token_dict[item['parent_token']], user_access_token_personal)
                    folder_token_dict[item['token']] = new_folder['token']
                    print(f"{item['name']}文件夹  在新账号创建成功")
                    print(f"{item['name']}文件夹  包含子文件夹，正在递归中...")
                    print('--------------------')
                    recurse_folder(item['token'])
                else:
                    modification_file_entity(item['token'], item['type'], user_access_token_ksyun)
                    print(f"{item['name']}文件  文件类型{item['type']}  文档权限已修改")
                    copy_file(item['token'], item['name'], item['type'], folder_token_dict[item['parent_token']], user_access_token_personal)
                    print(f"{item['name']}文件  文件类型{item['type']}  文档已成功复制至个人账号")
                    # modification_file_entity_rollback(item['token'], item['type'], user_access_token_ksyun)
                    # print(f"{item['name']}文件  文件类型{item['type']}  文档权限已修改回私密状态，并非原始状态")
                    print('--------------------')
        except Exception as e:
            print(e)

    recurse_folder(folder_token)
    print('所有任务已完成')
    return


if __name__ == "__main__":
    personal_root_folder_token = get_root_folder_meta(user_access_token_personal)['data']['token']
    ksyun_root_folder_token = get_root_folder_meta(user_access_token_ksyun)['data']['token']
    folder_token_dict = {ksyun_root_folder_token: personal_root_folder_token}

    main(ksyun_root_folder_token)
