from os import path

from Lib import resolve_path

_test_dir = resolve_path()
if not _test_dir.endswith("test"):
    _test_dir = path.join(_test_dir, "test")
_reset_dir = path.join(_test_dir, "test_files")
_bad_job_number_path = path.join(_reset_dir, "MicroVuExport_BadJobNumber.csv")
_bad_part_number_path = path.join(_reset_dir, "MicroVuExport_BadPartNumber.csv")
_bad_sequence_number_path = path.join(_reset_dir, "MicroVuExport_BadSequenceNumber.csv")
_missing_sequence_number_path = path.join(_reset_dir, "MicroVuExport_MissingSequenceNumber.csv")
_missing_part_number_path = path.join(_reset_dir, "MicroVuExport_MissingPartNumber.csv")
_missing_job_number_path = path.join(_reset_dir, "MicroVuExport_MissingJobNumber.csv")