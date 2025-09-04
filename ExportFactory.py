from CMMExport import CMMExport
from KeyenceExport import KeyenceExport
from MicroVuExport import MicroVuExport


def get_export(file_path: str) -> CMMExport | KeyenceExport | MicroVuExport | None:
    if file_path.endswith(".csv"):
        from CMMExport import CMMExport
        return CMMExport(file_path)
    elif file_path.endswith(".txt"):
        from KeyenceExport import KeyenceExport
        return KeyenceExport(file_path)
    elif file_path.endswith(".pdf"):
        from MicroVuExport import MicroVuExport
        return MicroVuExport(file_path)
    return None
