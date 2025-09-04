import os
from abc import ABC, abstractmethod


class ExportException(Exception):
    pass


class IExport(ABC):
    __file_path: str

    @abstractmethod
    def __init__(self, file_path: str):
        self.__file_path = file_path

    @property
    @abstractmethod
    def file_path(self):
        return self.__file_path

    @property
    def file_name(self):
        return os.path.basename(self.__file_path)

    @property
    @abstractmethod
    def operation(self):
        pass

    @property
    @abstractmethod
    def job_number(self):
        pass

    @property
    @abstractmethod
    def part_number(self):
        pass

    @property
    @abstractmethod
    def sequence_number(self):
        pass

