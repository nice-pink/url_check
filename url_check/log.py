from __future__ import annotations
from typing import Union
import os
from enum import Enum
import logging
from typing import Dict


class LogType(Enum):
    NoLog = 0
    Error = 1
    Warning = 2
    Info = 3
    All = 4

    @property
    def logstash_level(self) -> Union[logging.CRITICAL, logging.ERROR, logging.WARNING,
                                      logging.INFO, logging.DEBUG]:
        if self.name == 'NoLog':
            return logging.CRITICAL
        elif self.name == 'Error':
            return logging.ERROR
        elif self.name == 'Warning':
            return logging.WARNING
        elif self.name == 'Info':
            return logging.INFO
        elif self.name == 'All':
            return logging.DEBUG

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
