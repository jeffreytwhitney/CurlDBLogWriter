import sys
from os import path, getcwd


def get_file_lines(file_path: str) -> list[str]:
    if not file_path:
        return []
    with open(file_path, "r") as f:
        return f.readlines()


def resolve_path():
    return (
        path.abspath(path.dirname(sys.executable))
        if getattr(sys, "frozen", False)
        else path.abspath(path.join(getcwd()))
    )