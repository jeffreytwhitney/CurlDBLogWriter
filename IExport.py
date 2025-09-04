import os
from abc import ABC, abstractmethod
from typing import List


class InvalidFileFormatException(Exception):
    pass


class IExport(ABC):
    __file_path: str
    __job_number: str
    __part_number: str
    __sequence_numbers: List[int] = []

    @abstractmethod
    def __init__(self, file_path: str):
        self.__file_path = file_path

    @property
    def file_path(self) -> str:
        return self.__file_path

    @property
    def file_name(self) -> str:
        return os.path.basename(self.__file_path)

    @property
    def job_number(self) -> str:
        return self.__job_number

    @property
    def part_number(self) -> str:
        return self.__part_number

    @property
    def sequence_numbers(self) -> List[int]:
        return self.__sequence_numbers

