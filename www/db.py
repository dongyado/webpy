# db.py
# database engine

#database engine class
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

# 持有数据库链接的上下文对象
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return note self.connection is None

    def init(self):
        self.connection = _LasyConnection()
        self.transactions = 0


