# CurlDBLogWriter

CurlDBLogWriter reads a measurement export, extracts its part, job, and sequence numbers, and writes a log row for each sequence number to the SQL Server `xtblCurlLog` table. If an error message is supplied, it also maps that message to a display message using `ErrorDisplayMessages.xml`.

## Supported exports

| Export | Detection |
|---|---|
| CMM | `.xlsx` file |
| Keyence | First line starts with `PROGRAM NAME` |
| Micro-Vu | First line starts with `"TEXT PT: TEXT"` |

## Requirements

- Python 3.10 or newer
- Access to the target SQL Server database and permission to insert into `xtblCurlLog`

Install the runtime dependencies:

```bash
python -m pip install pymssql python-dotenv openpyxl
```

For the test suite, also install `pytest`:

```bash
python -m pip install pytest
```

## Configuration

Create a `.env` file in the working directory with the SQL Server connection settings:

```dotenv
DB_SERVER=your-server
DB_USER=your-user
DB_PASSWORD=your-password
DB_NAME=your-database
```

Keep database credentials private; do not commit a populated `.env` file. The application also reads logger levels from `CurlDBLogWriter.ini`. That file is included with `DEBUG` levels by default.

## Usage

Run the CLI from the project directory:

```bash
python CurlDBLogWriter.py --file path/to/export.csv --status 200 --machinename inspection-host
```

Provide an error message when logging a failed processing result:

```bash
python CurlDBLogWriter.py --file path/to/export.xlsx --status 500 --machinename inspection-host --errmsg "CMM file could not be parsed"
```

Options:

- `-f`, `--file`: Path to a supported export (required)
- `-s`, `--status`: Status code to record (required)
- `-m`, `--machinename`: Machine name to record (required)
- `-e`, `--errmsg`: Optional error message

Each extracted sequence number is logged as a separate row. Error display mappings can be adjusted in `ErrorDisplayMessages.xml`.

## Tests

Run the test suite from the project directory:

```bash
python -m pytest
```
