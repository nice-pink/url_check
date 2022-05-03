from enum import Enum

class LogType(Enum):
    NoLog = 0
    Error = 1
    Warning = 2
    Info = 3
    All = 4

class Log:
    """ LOG """
    
    @staticmethod
    def error(*args, **kwargs):
        message: str = " ".join(map(str, args))
        print("\033[1;31m" + message, **kwargs)

    @staticmethod
    def warning(*args, **kwargs):
        message: str = " ".join(map(str, args))
        print("\033[1;33m" + message, **kwargs)

    @staticmethod
    def info(*args, **kwargs):
        message: str = " ".join(map(str, args))
        print("\033[0m" + message, **kwargs)

    @staticmethod
    def happy(*args, **kwargs):
        message: str = " ".join(map(str, args))
        print("\033[1;32m" + message, **kwargs)
