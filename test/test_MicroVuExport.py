from os import path

from Lib import resolve_path
from MicroVuExport import MicroVuExport

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
_good_path = path.join(_reset_dir, "MicroVuExport_Good.csv")


def test_good_mv_export():
    export = MicroVuExport(_good_path)
    assert export.job_number == "8726476-002"
    assert export.file_name == "MicroVuExport_Good.csv"
    assert export.part_number == "M002776C001"
    assert export.sequence_numbers == [86]
