from CMMExport import CMMExport
from IExport import IExport
from KeyenceExport import KeyenceExport
from Lib import get_file_lines
from MicroVuExport import MicroVuExport


def get_export(file_path: str) -> IExport | None:
    if file_path.upper().endswith(".XLSX"):
        return CMMExport(file_path)

    file_lines = get_file_lines(file_path)
    if file_lines[0].upper().startswith("PROGRAM NAME"):
        return KeyenceExport(file_path)
    elif file_lines[0].upper().startswith("\"TEXT PT: TEXT\""):
        return MicroVuExport(file_path)
    return None
