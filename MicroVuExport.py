import os
from Lib import get_file_lines

from IExport import IExport, InvalidFileFormatException


class MicroVuExport(IExport):
    _file_path: str
    _job_number: str
    _part_number: str
    _sequence_numbers: list[int]
    _file_lines: list[str]

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self._file_lines = get_file_lines(file_path)
        self._parse_file_lines()

    def validate_file_lines(self):
        if len(self._file_lines) < 9:
            raise InvalidFileFormatException("MicroVu file is invalid.")
        if not self._file_lines[0].upper().startswith("\"TEXT PT: TEXT\""):
            raise InvalidFileFormatException("Part Number line is invalid.")
        if not self._file_lines[4].upper().startswith("\"PROMPT JOB: INPUT\""):
            raise InvalidFileFormatException("Job Number line is invalid.")
        if not self._file_lines[7].upper().startswith("\"PROMPT SEQUENCE: INPUT\""):
            raise InvalidFileFormatException("Sequence Number line is invalid.")

    def _parse_file_lines(self):
        pass

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def file_name(self) -> str:
        return os.path.basename(self._file_path)

    @property
    def job_number(self) -> str:
        return self._job_number

    @property
    def part_number(self) -> str:
        return self._part_number

    @property
    def sequence_numbers(self) -> list[int]:
        return self._sequence_numbers
