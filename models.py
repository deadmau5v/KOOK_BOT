class Role:
    """角色"""

    def __init__(self):
        self.role_id: int  # 角色 id
        self.name: str  # 角色名称
        self.color: int  # 颜色色值
        self.position: int  # 顺序位置
        self.hoist: int  # 是否为角色设定(与普通成员分开显示)
        self.mentionable: int  # 是否允许任何人@提及此角色
        self.permissions: int  # 权限码


class Quote:
    """引用的消息"""

    def __init__(self):
        self.id: str  # 引用消息 id
        self.type: int  # 引用消息类型
        self.content: str  # 引用消息内容
        self.create_at: int  # 引用消息创建时间（毫秒）
        self.author: dict  # 作者的用户信息


class Channel:
    def __init__(self):
        """频道"""
        self.id: str  # 频道 id
        self.name: str  # 频道名称
        self.user_id: str  # 创建者 id
        self.guild_id: str  # 服务器 id
        self.topic: str  # 频道简介
        self.is_category: bool  # 是否为分组，事件中为 int 格式
        self.parent_id: str  # 上级分组的 id (若没有则为 0 或空字符串)
        self.level: int  # 排序 level
        self.slow_mode: int  # 慢速模式下限制发言的最短时间间隔, 单位为秒(s)
        self.type: int  # 频道类型: 1 文字频道, 2 语音频道
        self.permission_overwrites: list[str]  # 针对角色在该频道的权限覆写规则组成的列表
        self.permission_users: list[str]  # 针对用户在该频道的权限覆写规则组成的列表
        self.permission_sync: int  # 权限设置是否与分组同步, 1 or 0
        self.has_password: bool  # 是否有密码


class Attachments:
    def __init__(self):
        """附加的多媒体"""
        self.type: str  # 多媒体类型
        self.url: str  # 多媒体地址
        self.name: str  # 多媒体名
        self.size: int  # 大小 单位 Byte


class User:
    def __init__(self):
        """用户"""
        self.id: str = ''
        self.username: str = ''
        self.nickname: str = ''
        self.identify_num: str = ''
        self.online: bool = False
        self.bot: bool = False
        self.status: int = 0
        self.avatar: str = ''
        self.vip_avatar: str = ''
        self.mobile_verified: bool = False
        self.roles: list[str] = []

    def __str__(self):
        return f"""
        ID: {self.id}
        Username: {self.username}
        Nickname: {self.nickname}
        Identify Number: {self.identify_num}
        Online: {self.online}
        Bot: {self.bot}
        Status: {self.status}
        Avatar: {self.avatar}
        VIP Avatar: {self.vip_avatar}
        Mobile Verified: {self.mobile_verified}
        Roles: {self.roles}\
"""


class Extra:
    def __init__(self):
        """消息数据"""
        # 1:文字消息,
        # 2:图片消息,
        # 3:视频消息,
        # 4:文件消息,
        # 8:音频消息,
        # 9:KMarkdown
        # 10:card 消息
        # 255:系统消息
        # 其它的暂未开放
        self.type: int = 0
        self.guild_id: str = ''  # 服务器 id
        self.channel_name: str = ''  # 频道名
        self.mention: list[str] = []  # 提及到的用户 id 的列表
        self.mention_all: bool = False  # 是否 mention 所有用户
        self.mention_roles: list[int] = []  # mention 用户角色的数组
        self.mention_here: bool = False  # 是否 mention 在线用户
        self.author: User | None = None  # 用户信息, 见 class User

    def __str__(self):
        return f"""
    Type: {self.type}
    Guild_id: {self.guild_id}
    Channel_name: {self.channel_name}
    Mention: {self.mention}
    Mention_all: {self.mention_all}
    Mention_roles: {self.mention_roles}
    Mention_here: {self.mention_here}
    Author: {self.author}\
"""


class Guild:
    def __init__(self):
        self.id: str  # 服务器 id
        self.name: str  # 服务器名称
        self.topic: str  # 服务器主题
        self.user_id: str  # 服务器主的 id
        self.icon: str  # 服务器 icon 的地址
        # 通知类型,
        # 0 代表默认使用服务器通知设置，
        # 1 代表接收所有通知,
        # 2 代表仅@被提及，
        # 3 代表不接收通知
        self.notify_type: int
        self.region: str  # 服务器默认使用语音区域
        self.enable_open: bool  # 是否为公开服务器
        self.open_id: str  # 公开服务器 id
        self.default_channel_id: str  # 默认频道 id
        self.welcome_channel_id: str  # 欢迎频道 id
        self.roles: list[str]  # 角色列表
        self.channels: list[str]  # 频道列表


class EventContent:
    def __init__(self):
        """事件内容"""
        # 消息通道类型,
        # GROUP 为组播消息,
        # PERSON 为单播消息,
        # BROADCAST 为广播消息
        self.channel_type: str = ''
        # 1:文字消息,
        # 2:图片消息,
        # 3:视频消息,
        # 4:文件消息,
        # 8:音频消息,
        # 9:KMarkdown
        # 10:card 消息
        # 255:系统消息
        # 其它的暂未开放
        self.type_: int = 0
        # 发送目的, 频道消息类时, 代表的是频道 channel_id，
        # 如果 channel_type 为 GROUP 组播且 type 为 255 系统消息时，则代表服务器 guild_id
        self.target_id: str = ''
        self.author_id: str = ''  # 发送者 id, 1 代表系统
        self.content: str = ''  # 消息内容, 文件，图片，视频时，content 为 url
        self.msg_id: str = ''  # 消息的 id
        self.msg_timestamp: int = 0  # 消息发送时间的毫秒时间戳
        self.nonce: str = ''  # 随机串，与用户消息发送 api 中传的 nonce 保持一致
        self.extra: Extra | None = None  # 不同的消息类型，结构不一致

    def debug(self):
        print(f"""\
Channel Type: {self.channel_type}
Type: {self.type_}
Target ID: {self.target_id}
Author ID: {self.author_id}
Content: {self.content}
Message ID: {self.msg_id}
Message Timestamp: {self.msg_timestamp}
Nonce: {self.nonce}
Extra: {self.extra}\
""")
