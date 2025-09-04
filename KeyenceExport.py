from IExport import IExport


class KeyenceExport(IExport):

    def __init__(self, file_path: str):
        super().__init__(file_path)
        super().__job_number = "Fred"
        super().__part_number = "1"
        super().__sequence_numbers = [1, 2, 3]

