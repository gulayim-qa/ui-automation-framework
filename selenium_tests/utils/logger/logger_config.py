import logging
import os


class LoggerConfig:
    """Class with logger config parameters."""

    LOGS_DIR_NAME = "selenium_tests/logs"
    LOGGER_NAME = "Logger"
    LOGS_FILE_NAME = LOGS_DIR_NAME + os.sep + "seleniumlog.log"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "[%(asctime)s] %(levelname)s %(message)s"
    CONSOLE_FORMAT = "[%(asctime)s] %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
