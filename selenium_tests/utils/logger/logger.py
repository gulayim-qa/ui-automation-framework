import logging
import os
import sys
from typing import Union
from selenium_tests.utils.logger.logger_config import LoggerConfig


class Logger:
    """Класс для настройки логгера и методов для изменения конфигурации логгера."""

    # Создаем директорию для логов, если она не существует
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)

    # Настройка логгера для записи в файл
    __file_logger = logging.getLogger(f"{LoggerConfig.LOGGER_NAME}_file")
    __file_logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __file_handler = logging.FileHandler(LoggerConfig.LOGS_FILE_NAME, mode="w", encoding="utf-8")
    __formatter = logging.Formatter(LoggerConfig.FORMAT, LoggerConfig.DATETIME_FORMAT)
    __file_handler.setFormatter(__formatter)
    __file_logger.addHandler(__file_handler)

    # Настройка логгера для вывода в консоль
    __console_logger = logging.getLogger(f"{LoggerConfig.LOGGER_NAME}_console")
    __console_logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __console_handler = logging.StreamHandler(sys.stdout)
    __console_formatter = logging.Formatter(LoggerConfig.CONSOLE_FORMAT, LoggerConfig.DATETIME_FORMAT)
    __console_handler.setFormatter(__console_formatter)
    __console_logger.addHandler(__console_handler)

    @staticmethod
    def set_level(level: Union[str, int]) -> None:
        """Устанавливает уровень логирования для обоих логгеров."""
        Logger.__file_logger.setLevel(level)
        Logger.__console_logger.setLevel(level)

    @staticmethod
    def info(message: str, to_file: bool = False) -> None:
        """Логирует сообщение с уровнем INFO."""
        if to_file:
            Logger.__file_logger.info(msg=message)
        else:
            Logger.__console_logger.info(msg=message)
            Logger.__file_logger.info(msg=message)

    @staticmethod
    def debug(message: str, to_file: bool = False) -> None:
        """Логирует сообщение с уровнем DEBUG."""
        if to_file:
            Logger.__file_logger.debug(msg=message)
        else:
            Logger.__console_logger.debug(msg=message)
            Logger.__file_logger.debug(msg=message)

    @staticmethod
    def warning(message: str, to_file: bool = False) -> None:
        """Логирует сообщение с уровнем WARNING."""
        if to_file:
            Logger.__file_logger.warning(msg=message)
        else:
            Logger.__console_logger.warning(msg=message)
            Logger.__file_logger.warning(msg=message)

    @staticmethod
    def error(message: str, to_file: bool = False) -> None:
        """Логирует сообщение с уровнем ERROR."""
        if to_file:
            Logger.__file_logger.error(msg=message)
        else:
            Logger.__console_logger.error(msg=message)
            Logger.__file_logger.error(msg=message)

    @staticmethod
    def fatal(message: str, to_file: bool = False) -> None:
        """Логирует сообщение с уровнем FATAL."""
        if to_file:
            Logger.__file_logger.fatal(msg=message)
        else:
            Logger.__console_logger.fatal(msg=message)
            Logger.__file_logger.fatal(msg=message)
