from logging import StreamHandler, Formatter
from logging import Logger
from constants import LOG_LEVEL
from collections import defaultdict
from sys import stdout


class BaseLogger(Logger):
    levels = defaultdict(
        lambda: 20,
        {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40, "CRITICAL": 50},
    )

    def __init__(self):
        super().__init__(__name__)
        stream_handler = StreamHandler(stdout)
        fmt = Formatter("[%(levelname)s] (%(asctime)s) : %(message)s")
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)
        self.setLevel(self.levels[LOG_LEVEL])


base_logger = BaseLogger()
