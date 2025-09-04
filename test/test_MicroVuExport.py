from os import path

from Lib import resolve_path

_test_dir = resolve_path()
if not _test_dir.endswith("test"):
    _test_dir = path.join(_test_dir, "test")
_reset_dir = path.join(_test_dir, "test_files")
