import logging.handlers
import queue
from PySide6.QtCore import QThread, Signal
from ui.settings import TEMP_DIR

log_queue = queue.Queue()
logger = logging.getLogger("logger")  # 创建一个日志记录器
file_handler = logging.handlers.QueueHandler(log_queue)
file_handler.setFormatter(logging.Formatter(f'[%(levelname)s %(asctime)s] %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(TEMP_DIR / "run.log")
file_handler.setFormatter(logging.Formatter(f'[%(levelname)s %(asctime)s] %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class LoggerThread(QThread):
    sig_logger = Signal(str)

    def run(self) -> None:
        while True:
            record = log_queue.get()
            self.sig_logger.emit(record.message)
