import DB
from ErrorDisplayMapper import ErrorDisplayMapper
from IExport import IExport


def write_log_entry(machine_name: str, status_code: int, error_message: str, export: IExport):
    error_display_message = ""
    if len(error_message.strip()) > 0:
        if export.file_name.upper().find("SORT") > -1:
            error_display_message = "Sort"
        else:
            error_display_message = ErrorDisplayMapper().get_error_display_message(error_message)

    with DB.DatabaseConnection(False) as dbc:
        for sequence_number in export.sequence_numbers:
            if error_message:
                sql = f"""INSERT INTO xtblCurlLog (FileName, Program, JobNumber, SequenceNumber, ErrorMessage, StatusCode, MachineName, ErrorMessageDisplay) VALUES ('{export.file_name}', '{export.part_number}', '{export.job_number}', {sequence_number}, '{error_message}', {status_code}, '{machine_name}', '{error_display_message}')"""
            else:
                sql = f"""INSERT INTO xtblCurlLog (FileName, Program, JobNumber, SequenceNumber, StatusCode, MachineName) VALUES ('{export.file_name}', '{export.part_number}', '{export.job_number}', {sequence_number}, {status_code}, '{machine_name}')"""
            dbc.execute_statement(sql)
