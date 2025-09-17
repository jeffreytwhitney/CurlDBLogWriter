import os
from dataclasses import dataclass

import pytest

from ErrorDisplayMapper import ErrorDisplayMapper
from Lib import resolve_path, get_file_lines


@dataclass
class LogErrorRow:
    is_default_error: bool
    message: str
    display_message: str


@pytest.fixture()
def log_error_rows():
    log_error_rows = []
    current_dir = resolve_path()
    if not current_dir.endswith("test"):
        current_dir = os.path.join(current_dir, "test")
    log_error_path = os.path.join(current_dir, "LogErrors.txt")
    if os.path.exists(log_error_path):
        file_rows = get_file_lines(log_error_path)
        for row in file_rows:
            if row != "":
                log_error_rows.append(LogErrorRow(False, row, ""))
        return log_error_rows
    return []


def test_does_not_match_selected_inspection():
    error_mapper = ErrorDisplayMapper()
    error_message = "PARSING: CMM file does not match selected inspection or balloon numbers are missing."
    assert error_mapper.get_error_display_message(error_message) == "CMM file does nor match selected inspection or balloon numbers are missing."


def test_balloon():
    error_mapper = ErrorDisplayMapper()
    error_message = "PARSING:  Balloon #7 has more places: (2), than in the spec: (1)."
    assert error_mapper.get_error_display_message(error_message) == "Balloon"


def test_could_not_be_parsed():
    error_mapper = ErrorDisplayMapper()
    error_message = "PARSING: CMM file could not be parsed or does not match the inspection plan. Make sure all specs in the plan match the CMM output."
    assert error_mapper.get_error_display_message(error_message) == "CMM file could not be parsed or does not match the inspection plan. Make sure all specs in the plan match the CMM output."


def test_all_log_error_rows(log_error_rows):
    error_mapper = ErrorDisplayMapper()
    for row in log_error_rows:
        error_message = row.message
        error_display_message = error_mapper.get_error_display_message(error_message)
        row.display_message = error_display_message
        if error_display_message == "Unknown Error":
            row.is_default_error = True
    unknown_errors = [row for row in log_error_rows if row.is_default_error is True]
    unknown_parser_errors = [row for row in log_error_rows if row.display_message == "Unknown Parsing Error"]
    unknown_header_errors = [row for row in log_error_rows if row.display_message == "Unknown Header Error"]
    assert len(unknown_errors) == 1
    assert len(unknown_parser_errors) == 1
    assert len(unknown_header_errors) == 1
