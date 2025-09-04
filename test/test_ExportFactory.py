from os import path

import ExportFactory
from CMMExport import CMMExport
from MicroVuExport import MicroVuExport
from KeyenceExport import KeyenceExport
from Lib import resolve_path

_test_dir = resolve_path()
if not _test_dir.endswith("test"):
    _test_dir = path.join(_test_dir, "test")
_reset_dir = path.join(_test_dir, "test_files")


def test_cmm_export():
    cmm_filepath = path.join(_reset_dir, "CMM Export.xlsx")
    export = ExportFactory.get_export(cmm_filepath)
    assert isinstance(export, CMMExport)


def test_microvu_export_factory():
    microvu_filepath = path.join(_reset_dir, "MicroVuExport_Good.csv")
    export = ExportFactory.get_export(microvu_filepath)
    assert isinstance(export, MicroVuExport)


def test_single_part_keyence_export_factory():
    keyence_filepath = path.join(_reset_dir, "SinglePartKeyence.csv")
    export = ExportFactory.get_export(keyence_filepath)
    assert isinstance(export, KeyenceExport)


def test_multi_part_keyence_export_factory():
    keyence_filepath = path.join(_reset_dir, "MultiPartKeyence.csv")
    export = ExportFactory.get_export(keyence_filepath)
    assert isinstance(export, KeyenceExport)
