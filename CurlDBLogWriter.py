import sys
from optparse import OptionParser

import DBLogWriter
import ExportFactory

n = len(sys.argv)
if n > 1:
    opt_parser = OptionParser(
        usage="%prog -f <file_path> -s <status_code> -m <machine_name> [-e <error_message>]",
        description="Write a log entry to the database-backed export selected for the provided file path.",
        epilog="Examples:\n  %prog -f /path/to/file.csv -s 200 -m my-host\n  %prog --file data.xlsx --status 500 --machinename ci-runner --errmsg \"Validation failed\""
    )
    opt_parser.add_option("-f", "--file", dest="file_path", type="string", help="File path (required)")
    opt_parser.add_option("-s", "--status", dest="status_code", help="Status code (required)")
    opt_parser.add_option("-e", "--errmsg", dest="error_message", help="Error message (optional)")
    opt_parser.add_option("-m", "--machinename", dest="machine_name", help="Machine name (required)")
    (options, args) = opt_parser.parse_args()

    # Validate required arguments
    missing = []
    if not options.file_path:
        missing.append("--file")
    if not options.status_code:
        missing.append("--status")
    if not options.machine_name:
        missing.append("--machinename")

    if missing:
        sys.stderr.write("Error: missing required option(s): " + ", ".join(missing) + "\n\n")
        opt_parser.print_help()
        sys.exit(2)

    IExport = ExportFactory.get_export(options.file_path)

    DBLogWriter.write_log_entry(options.machine_name, options.status_code, options.error_message, IExport)

    sys.exit(0)
else:
    opt_parser = OptionParser(
        usage="%prog -f <file_path> -s <status_code> -m <machine_name> [-e <error_message>]",
        description="Write a log entry to the database-backed export selected for the provided file path.",
        epilog="Examples:\n  %prog -f /path/to/file.csv -s 200 -m my-host\n  %prog --file data.xlsx --status 500 --machinename ci-runner --errmsg \"Validation failed\""
    )
    opt_parser.add_option("-f", "--file", dest="file_path", type="string", help="File path (required)")
    opt_parser.add_option("-s", "--status", dest="status_code", help="Status code (required)")
    opt_parser.add_option("-e", "--errmsg", dest="error_message", help="Error message (optional)")
    opt_parser.add_option("-m", "--machinename", dest="machine_name", help="Machine name (required)")
    # Show help when no arguments are provided
    opt_parser.print_help()
    sys.exit(2)
