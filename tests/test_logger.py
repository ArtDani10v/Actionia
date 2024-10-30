# tests/test_logger.py

import os
import sys
import pytest

# Добавление пути к backend для импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from utils.logger import log_info, log_error, LOG_FILE

def test_log_info():
    log_info("Тестовое информационное сообщение.", "TestFunction")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.read()
    assert "TestFunction - Тестовое информационное сообщение." in logs

def test_log_error():
    log_error("Тестовое сообщение об ошибке.", "TestFunction")
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = f.read()
    assert "TestFunction - Тестовое сообщение об ошибке." in logs
