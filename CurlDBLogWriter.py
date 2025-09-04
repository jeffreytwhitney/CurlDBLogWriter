import sys
from optparse import OptionParser

import DBLogWriter
import ExportFactory

n = len(sys.argv)
if n > 1:
    opt_parser = OptionParser()
    opt_parser.add_option("-f", "--file", dest="file_path", type="string", help="File path")
    opt_parser.add_option("-s", "--status", dest="status_code", help="Status code")
    opt_parser.add_option("-e", "--errmsg", dest="error_message", help="Error message")
    opt_parser.add_option("-m", "--machinename", dest="machine_name", help="Machine name")
    (options, args) = opt_parser.parse_args()
    IExport = ExportFactory.get_export(options.file_path)

    DBLogWriter.write_log_entry(options.machine_name, options.status_code, options.error_message, IExport)

    sys.exit(0)
