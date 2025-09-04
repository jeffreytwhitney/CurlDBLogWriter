import os
from abc import ABC, abstractmethod
from typing import List


class InvalidFileFormatException(Exception):
    pass


class IExport(ABC):

    @abstractmethod
    def __init__(self, file_path: str):
        self.__file_path = file_path

    @property
    @abstractmethod
    def file_path(self) -> str:
        pass

    @property
    @abstractmethod
    def file_name(self) -> str:
        pass

    @property
    @abstractmethod
    def job_number(self) -> str:
        pass

    @property
    @abstractmethod
    def part_number(self) -> str:
        pass

    @property
    @abstractmethod
    def sequence_numbers(self) -> List[int]:
        pass

