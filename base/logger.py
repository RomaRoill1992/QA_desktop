import datetime
import os


class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now()) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls):
        testname = os.environ('PYTEST_CURRENT_TEST')