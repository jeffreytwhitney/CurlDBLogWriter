from KeyenceExport import KeyenceExport


def test_single_part_keyence(keyence_filepath: str):
    export = KeyenceExport(keyence_filepath)
    assert export.job_number == "29831000-014"
    assert export.file_name == "SinglePartKeyence.csv"
    assert export.part_number == "3000791"
    assert export.sequence_numbers == [7]


def test_multi_part_keyence(keyence_multi_part_filepath: str):
    export = KeyenceExport(keyence_multi_part_filepath)
    assert export.job_number == "29781600-005"
    assert export.file_name == "MultiPartKeyence.csv"
    assert export.part_number == "100165732"
    assert export.sequence_numbers == [426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464]
