
from smb.SMBConnection import SMBConnection


class DirectoryMager():

    def __init__(ip, port, user_name, password):
        import pudb; pudb.set_trace()  # XXX BREAKPOINT
        self.connection = None
        self.server_ip = ip
        self.server_port = port
        self.user_name = user_name
        self.password = password


    def list_shared_directories():
        raise NotImplementedError

    def connect():
        raise NotImplementedError

    def upload_file():
        raise NotImplementedError

    def get_file():
        raise NotImplementedError


class SMBManager(DirectoryMager):

    def __init__(ip, port, user_name, password):
        import pudb; pudb.set_trace()  # XXX BREAKPOINT
        self.connection = SMBConnection()

    def list_shared_directories():
        pass


if __name__ == 'main':
    smb_manager = SMBManager(1,2,5,7)
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    assert 1 == 1

