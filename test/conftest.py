from os import path

import pytest

from Lib import resolve_path


@pytest.fixture(scope="session")
def test_dir():
    test_dir = resolve_path()
    if not test_dir.endswith("test"):
        test_dir = path.join(test_dir, "test")
    return test_dir


@pytest.fixture(scope="session")
def reset_dir(test_dir):
    reset_dir = path.join(test_dir, "test_files")
    return reset_dir


@pytest.fixture(scope="session")
def mv_bad_job_number_path(reset_dir):
    bad_job_number_path = path.join(reset_dir, "MicroVuExport_BadJobNumber.csv")
    return bad_job_number_path


@pytest.fixture(scope="session")
def mv_bad_part_number_path(reset_dir):
    bad_part_number_path = path.join(reset_dir, "MicroVuExport_BadPartNumber.csv")
    return bad_part_number_path


@pytest.fixture(scope="session")
def mv_bad_sequence_number_path(reset_dir):
    bad_sequence_number_path = path.join(reset_dir, "MicroVuExport_BadSequenceNumber.csv")
    return bad_sequence_number_path


@pytest.fixture(scope="session")
def mv_missing_sequence_number_path(reset_dir):
    missing_sequence_number_path = path.join(reset_dir, "MicroVuExport_MissingSequenceNumber.csv")
    return missing_sequence_number_path


@pytest.fixture(scope="session")
def mv_missing_part_number_path(reset_dir):
    missing_part_number_path = path.join(reset_dir, "MicroVuExport_MissingPartNumber.csv")
    return missing_part_number_path


@pytest.fixture(scope="session")
def mv_missing_job_number_path(reset_dir):
    missing_job_number_path = path.join(reset_dir, "MicroVuExport_MissingJobNumber.csv")
    return missing_job_number_path


@pytest.fixture(scope="session")
def mv_good_path(reset_dir):
    good_path = path.join(reset_dir, "MicroVuExport_Good.csv")
    return good_path


@pytest.fixture(scope="session")
def cmm_filepath(reset_dir):
    cmm_filepath = path.join(reset_dir, "CMM Export.xlsx")
    return cmm_filepath


@pytest.fixture(scope="session")
def keyence_filepath(reset_dir):
    keyence_filepath = path.join(reset_dir, "SinglePartKeyence.csv")
    return keyence_filepath


@pytest.fixture(scope="session")
def keyence_multi_part_filepath(reset_dir):
    keyence_filepath = path.join(reset_dir, "MultiPartKeyence.csv")
    return keyence_filepath
