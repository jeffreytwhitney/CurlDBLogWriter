import logging

import LocalLogger


def test_log_level():
    logger = LocalLogger.get_logger("curl_db_log_writer_logger")
    current_level = logger.getEffectiveLevel()
    level_name = logging.getLevelName(current_level)
    assert level_name == "DEBUG"
