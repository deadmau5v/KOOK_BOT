import requests

import models
from env import token, BOTID, BASEAPI

events_dict = {}


headers = {
    f"Authorization": "Bot {token}"
}


def regain(typeof: str):
    """注册事件"""

    def outer(func):
        events_dict[typeof] = func
        return func

    return outer


class Event:
    def __init__(self, data: dict):
        self.data = data
        self.event = models.EventContent()
        self.event.extra = models.Extra()
        self.event.extra.author = models.User()
        extra_data = data.get('extra', {})
        author_data = extra_data.get('author', {})

        self.event.type_ = data.get('type')
        self.event.content = data.get('content')
        self.event.nonce = data.get('nonce')
        self.event.msg_id = data.get('msg_id')
        self.event.author_id = data.get('author_id')
        self.event.channel_type = data.get('channel_type')
        self.event.msg_timestamp = data.get('msg_timestamp')
        self.event.target_id = data.get('target_id')

        if extra_data:
            self.event.extra.type = extra_data.get('type')
            self.event.extra.mention = extra_data.get('mention')
            self.event.extra.guild_id = extra_data.get('guild_id')
            self.event.extra.channel_name = extra_data.get('channel_name')
            self.event.extra.mention_all = extra_data.get('mention_all')
            self.event.extra.mention_here = extra_data.get('mention_here')
            self.event.extra.mention_roles = extra_data.get('mention_roles')

        if author_data:
            self.event.extra.author.id = author_data.get('id')
            self.event.extra.author.username = author_data.get('username')
            self.event.extra.author.nickname = author_data.get('nickname')
            self.event.extra.author.identify_num = author_data.get('identify_num')
            self.event.extra.author.online = author_data.get('online')
            self.event.extra.author.bot = author_data.get('bot')
            self.event.extra.author.status = author_data.get('status')
            self.event.extra.author.avatar = author_data.get('avatar')
            self.event.extra.author.vip_avatar = author_data.get('vip_avatar')
            self.event.extra.author.mobile_verified = author_data.get('mobile_verified')
            self.event.extra.author.roles = author_data.get('roles')

        self.event.debug()

        self.result = self.switch()

    @regain("9")
    def message(self):
        """消息回调"""
        if self.event.channel_type == "GROUP":
            guild_name = requests.get(BASEAPI + "/api/v3/guild/view", {"guild_id": self.event.extra.guild_id},
                                      headers=headers).json()
            res = f"[{guild_name['data']['name']}][{self.event.extra.channel_name}][{self.event.extra.author.nickname}]: {self.event.content}"
        else:
            res = f"[{self.event.extra.author.nickname}]: {self.event.content}"

        # 匹配命令
        if BOTID in self.event.extra.mention:
            print("被提及")

            if self.event.content.strip() == f"(met){BOTID}(met) /help":
                pass
            else:
                requests.post(BASEAPI + "/api/v3/message/create", headers=headers, json={
                    "type": 10,
                    "target_id": self.event.target_id,
                    # 消息卡片
                    "content": '''[
                                  {
                                    "type": "card",
                                    "size": "lg",
                                    "theme": "info",
                                    "modules": [
                                      {
                                        "type": "header",
                                        "text": {
                                          "type": "plain-text",
                                          "content": "DEV BOT"
                                        }
                                      },
                                      {
                                        "type": "divider"
                                      },
                                      {
                                        "type": "section",
                                        "mode": "right",
                                        "accessory": {
                                          "type": "button",
                                          "theme": "primary",
                                          "value": "help",
                                          "text": {
                                            "type": "plain-text",
                                            "content": "/help"
                                          }
                                        },
                                        "text": {
                                          "type": "kmarkdown",
                                          "content": "**使用 /help 获取帮助**"
                                        }
                                      },
                                      {
                                        "type": "divider"
                                      }
                                    ]
                                  }
                                ]''',
                    "quote": self.event.msg_id,
                })

        print(res)
        return {}

    @regain("255")
    def verify(self):
        """验证BOT调用"""
        try:
            return {"challenge": self.data["challenge"]}
        except KeyError:
            print(self.data)
            return self.data

    @regain("message_btn_click")
    def click(self):
        print("hello")
        return {}

    def switch(self):
        """分发事件"""
        if events_dict.get(str(self.event.type_)):
            return events_dict[str(self.event.type_)](self)
        else:
            print(f"未知事件: {self.data['type']}")
            return {}
