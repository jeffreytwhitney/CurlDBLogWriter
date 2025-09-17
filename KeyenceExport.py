import os

from IExport import IExport
from Lib import get_file_lines


class KeyenceExport(IExport):
    _file_path: str
    _job_number: str
    _part_number: str
    _sequence_numbers: list[int] = []
    _file_lines: list[str] = []

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self._sequence_numbers = []
        self._file_path = file_path
        self._file_lines = get_file_lines(file_path)
        self._parse_file_lines()

    def _parse_file_lines(self):
        line_count = len(self._file_lines)
        self._part_number = self._file_lines[4].split(",")[0]
        if "_" in self._part_number:
            self._part_number = self._part_number.split("_")[0]
        self._job_number = self._file_lines[4].split(",")[5]

        for i in range(4, line_count):
            line = self._file_lines[i]
            if line == "":
                continue
            seq_nbr = line.split(",")[2]
            self._sequence_numbers.append(int(seq_nbr))

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def job_number(self) -> str:
        return self._job_number

    @property
    def part_number(self) -> str:
        return self._part_number

    @property
    def sequence_numbers(self) -> list[int]:
        return self._sequence_numbers

    @property
    def file_name(self) -> str:
        return os.path.basename(self._file_path)
