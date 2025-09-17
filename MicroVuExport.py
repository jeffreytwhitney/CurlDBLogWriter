import os

from IExport import IExport
from Lib import get_file_lines


def get_node_text(file_lines: list[str], search_value: str, start_delimiter: str, end_delimiter: str = "") -> str:
    line_index: int = next((i for i, l in enumerate(file_lines) if l.upper().find(search_value.upper()) > 0), -1)
    if line_index == -1:
        return ""

    line_text = file_lines[line_index]
    return line_text.split(",")[1].strip("[\"\n]")


class MicroVuExport(IExport):
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
        self._part_number = get_node_text(self._file_lines, "Text PT: Text", "\"")
        self._job_number = get_node_text(self._file_lines, "Prompt JOB: Input", "\"")
        seq_nbr = get_node_text(self._file_lines, "Prompt SEQUENCE: Input", "\"")
        if seq_nbr == "":
            if -1 not in self._sequence_numbers:
                self._sequence_numbers.append(-1)
        else:
            if int(seq_nbr) not in self._sequence_numbers:
                self._sequence_numbers.append(int(seq_nbr))

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

    def clear(self):
        self._file_lines = []
        self._sequence_numbers = []
        self._part_number = ""
        self._job_number = ""
        self._file_path = ""
