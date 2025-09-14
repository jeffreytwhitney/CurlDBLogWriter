import DB
from IExport import IExport


def write_log_entry(machine_name: str, status_code: int, error_message: str, export: IExport):
    with DB.DatabaseConnection(False) as db:
        for sequence_number in export.sequence_numbers:
            sql = f"""INSERT INTO xtblCurlLog (FileName, Program, JobNumber, SequenceNumber, ErrorMessage, StatusCode, MachineName) VALUES ('{export.file_name}', '{export.part_number}', '{export.job_number}', {sequence_number}, '{error_message}', {status_code}, '{machine_name}')"""
            db.execute_sql_statement(sql)
