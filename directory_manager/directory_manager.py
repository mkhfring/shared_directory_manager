
from smb.SMBConnection import SMBConnection


class DirectoryMager():

    def __init__(self, ip, user_name, password, server_name=None, port=None):
        self.connection = None
        self.server_ip = ip
        self.server_port = port
        self.user_name = user_name
        self.password = password
        self.server_name = server_name

    def list_shared_directories(self):
        raise NotImplementedError

    def _connect(self):
        raise NotImplementedError

    def upload_file(self):
        raise NotImplementedError

    def get_file(self):
        raise NotImplementedError


class SMBManager(DirectoryMager):

    def __init__(self, ip, user_name, password, server_name, port=445):
        super().__init__(ip, user_name, password, server_name, port)

    def _list_shared_directories(self):
        if not self.connection:
            self._connect()

        shares = self.connection.listShares()
        shared_directories = [
            share.name for share in shares\
            if not share.isSpecial and share.name not in [
                'NETLOGON',
                'SYSVOL'
            ]
        ]

        return shared_directories


    def _connect(self):
        self.connection = SMBConnection(
            self.user_name,
            self.password,
            self.server_ip,
            self.server_name,
            is_direct_tcp=True
        )
        is_connected = self.connection.connect(
            self.server_ip,
            self.server_port
        )
        return is_connected

    @property
    def get_shared_directory(self):
        shared_directories = self._list_shared_directories()
        if len(shared_directories) > 0:
            return shared_directories[0]

