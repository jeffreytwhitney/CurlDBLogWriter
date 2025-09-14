from MicroVuExport import MicroVuExport


def test_good_mv_export(mv_good_path: str):
    export = MicroVuExport(mv_good_path)
    assert export.job_number == "8726476-002"
    assert export.file_name == "MicroVuExport_Good.csv"
    assert export.part_number == "M002776C001"
    assert export.sequence_numbers == [86]


def test_bad_job_number_mv_export(mv_bad_job_number_path: str):
    export = MicroVuExport(mv_bad_job_number_path)
    assert export.job_number == ""
    assert export.file_name == "MicroVuExport_BadJobNumber.csv"
    assert export.part_number == "M002776C001"
    assert export.sequence_numbers == [86]


def test_bad_part_number_mv_export(mv_bad_part_number_path: str):
    export = MicroVuExport(mv_bad_part_number_path)
    assert export.job_number == "8726476-002"
    assert export.file_name == "MicroVuExport_BadPartNumber.csv"
    assert export.part_number == ""
    assert export.sequence_numbers == [86]


def test_missing_job_number_mv_export(mv_missing_job_number_path: str):
    export = MicroVuExport(mv_missing_job_number_path)
    assert export.job_number == ""
    assert export.file_name == "MicroVuExport_MissingJobNumber.csv"
    assert export.part_number == "M002776C001"
    assert export.sequence_numbers == [86]


def test_missing_part_number_mv_export(mv_missing_part_number_path: str):
    export = MicroVuExport(mv_missing_part_number_path)
    assert export.job_number == "8726476-002"
    assert export.file_name == "MicroVuExport_MissingPartNumber.csv"
    assert export.part_number == ""
    assert export.sequence_numbers == [86]


def test_bad_sequence_number_mv_export(mv_bad_sequence_number_path: str):
    bad_export = MicroVuExport(mv_bad_sequence_number_path)
    assert bad_export.job_number == "8726476-002"
    assert bad_export.file_name == "MicroVuExport_BadSequenceNumber.csv"
    assert bad_export.part_number == "M002776C001"
    assert 0 in bad_export.sequence_numbers


def test_missing_sequence_number_mv_export(mv_missing_sequence_number_path: str):
    export = MicroVuExport(mv_missing_sequence_number_path)
    assert export.job_number == "8726476-002"
    assert export.file_name == "MicroVuExport_MissingSequenceNumber.csv"
    assert export.part_number == "M002776C001"
    assert export.sequence_numbers == [0]
