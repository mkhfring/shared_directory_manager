class ConnectionException(Exception):
    status = None

    def __init__(self, status=None):
        if status is not None:
            self.status = status

        super().__init__(self.status)


class NoDirectoryException(Exception):
    status = None

    def __init__(self, status=None):
        if status is not None:
            self.status = status

        super().__init__(self.status)
