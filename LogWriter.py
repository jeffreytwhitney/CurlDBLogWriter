class LogWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_log_entry(self, message):
        with open(self.filename, 'a') as f:
            f.write(message)
