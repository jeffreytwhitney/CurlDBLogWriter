import sys

from MicroVuExportParser import MicroVuExportParser

n = len(sys.argv)
if n > 1:
    for arg in range(1, n):
        mv_parser = MicroVuExportParser(sys.argv[arg])
        mv_parser.process_file()

    sys.exit(0)