import re

from ErrorDisplayParser import ErrorDisplayEntry, ErrorDisplayParser


class ErrorDisplayMapper:
    _error_display_records: list[ErrorDisplayEntry] = []

    def __init__(self):
        self._error_display_records = []
        self._error_display_records = ErrorDisplayParser().get_error_display_messages()

    def get_error_display_message(self, error_message: str) -> str:
        for error_display_record in self._error_display_records:
            regex_pattern = error_display_record.regex
            match = re.search(regex_pattern, error_message)
            if match:
                return error_display_record.message
        default_record = [e for e in self._error_display_records if e.is_default is True]
        return default_record[0].message
