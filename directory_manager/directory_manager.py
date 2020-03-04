from smb.SMBConnection import SMBConnection
from .exceptions import ConnectionException, NoDirectoryException


class DirectoryMager():

    def __init__(self, ip, user_name, password, server_name=None, port=None):
        self.connection = None
        self.server_ip = ip
        self.server_port = port
        self.user_name = user_name
        self.password = password
        self.server_name = server_name

    def _list_shared_directories(self):
        raise NotImplementedError

    def _connect(self):
        raise NotImplementedError

    def _disconnect(self):
        raise NotImplementedError

    def put_file(self):
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
        self._disconnect()
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
        if not is_connected:
            raise ConnectionException('Fail to connect to the samba server')

        return self.connection

    def _disconnect(self):
        self.connection.close()
        self.connection = None

    def put_file(self, local_file_path, samba_file_path):
        pass

    def get_file(self, samba_file_path, local_file_path):
        shared_directory = self.get_shared_directory
        if not self.connection:
            self._connect()

        with open(local_file_path, 'wb') as file_obj:
            try:
                file_attribute, file_size = self.connection.retrieveFile(
                    shared_directory,
                    samba_file_path,
                    file_obj
                )
            except Exception as e:
                raise e

            finally:
                self._disconnect()

        return (file_attribute, file_size)


    @property
    def get_shared_directory(self):

        #todo: Take care if there are more than one shared directory
        shared_directories = self._list_shared_directories()
        if len(shared_directories) == 0:
            raise NoDirectoryException('No Directory Is Shared')

        return shared_directories[0]

