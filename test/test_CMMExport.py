from CMMExport import CMMExport


def test_good_mv_export(cmm_filepath: str):
    export = CMMExport(cmm_filepath)
    assert export.job_number == "8726398-002"
    assert export.file_name == "CMM Export.xlsx"
    assert export.part_number == "82086 01 01"
    assert export.sequence_numbers == [40]
