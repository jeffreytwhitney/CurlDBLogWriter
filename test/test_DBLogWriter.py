from unittest.mock import patch, MagicMock

import DBLogWriter
import ExportFactory


def test_write_log_entry_executes_sql_for_each_sequence_number(mv_good_path):
    export = ExportFactory.get_export(mv_good_path)
    machine_name = "Y-006"
    status_code = 2
    error_message = "SUCCESS"

    with patch("DBLogWriter.DB.DatabaseConnection") as DatabaseConnection:
        db_mock = MagicMock()
        DatabaseConnection.return_value.__enter__.return_value = db_mock

        DBLogWriter.write_log_entry(machine_name, status_code, error_message, export)

        # One call per sequence number
        assert db_mock.execute_sql_statement.call_count == len(export.sequence_numbers)

        for call, seq in zip(db_mock.execute_sql_statement.call_args_list, export.sequence_numbers):
            sql = call.args[0]
            assert "INSERT INTO xtblCurlLog" in sql
            assert f"'{export.file_name}'" in sql
            assert f"'{export.part_number}'" in sql
            assert f"'{export.job_number}'" in sql
            # sequence number is numeric, appears unquoted surrounded by commas and/or spaces
            assert f", {seq}," in sql or f", {seq} ," in sql
            assert f"'{error_message}'" in sql
            assert f", {status_code}," in sql or f", {status_code} ," in sql
            assert f"'{machine_name}'" in sql
