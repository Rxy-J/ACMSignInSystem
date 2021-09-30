class ConnectError(Exception):

    def __init__(self, *args, **kwargs):
        super(ConnectError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "连接失败，请检查网络连接"


class FileError(Exception):

    def __init__(self, *args, **kwargs):
        super(FileError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "创建或读写文件失败，请检查路径及文件读写权限"


class LoginError(Exception):

    def __init__(self, *args, **kwargs):
        super(LoginError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "登录失败，请检查账号密码"


class DbConnectError(Exception):

    def __init__(self, *args, **kwargs):
        super(DbConnectError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "数据库连接错误"


class DbError(Exception):

    def __init__(self, *args, **kwargs):
        super(DbError, self).__init__(*args, **kwargs)

    def __str__(self):
        return "数据库操作错误"
