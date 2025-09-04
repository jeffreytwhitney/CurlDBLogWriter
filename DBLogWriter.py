import DB
from IExport import IExport


def write_log_entry(self, machine_name: str, status_code: int, error_message: str, export: IExport):
    sql = f"""INSERT INTO xtblCurlLog (FileName, Program, JobNumber, SequenceNumber, ErrorMessage,
    StatusCode, MachineName) VALUES ('{export.file_name}', '{export.part_number}', '{export.job_number}', 
    {export.sequence_number}, '{error_message}', {status_code}, '{machine_name}')"""
    DB.execute_sql_statement(sql)
