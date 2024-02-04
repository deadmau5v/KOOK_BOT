import os

# 环境变量读取
# KOOK_BOT_TOKEN : 机器人token
# KOOK_BOT_ID     : 机器人ID


BASEAPI = "https://www.kookapp.cn"

try:
    token = os.environ['KOOK_BOT_TOKEN']
except KeyError:
    print("请设置环境变量 KOOK_BOT_TOKEN https://developer.kookapp.cn/bot/information")
    exit(-1)

try:
    BOTID = os.environ['KOOK_BOT_ID']
except KeyError:
    print("请设置环境变量 KOOK_BOT_ID, 在群聊中 右侧列表右键机器人 最下面的选项复制ID即可获得BOTID")
    exit(-1)

try:
    EncryptKey = os.environ["KOOK_ENCRYPT_KEY"]
except KeyError:
    print("请设置 KOOK_ENCRYPT_KEY https://developer.kookapp.cn/bot/information")
    exit(-1)