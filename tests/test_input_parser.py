import os

from marski_group_solver.input_parser import (
    parse_all_students_file,
    parse_banned_combinations_file,
)


def test_parse_all_students_file(example_students_list):
    # Assuming the 'test_data' directory is in the same directory as the test module
    file_path = os.path.join(os.path.dirname(__file__), "test_data", "all_students.txt")
    result = parse_all_students_file(file_path)
    assert result == example_students_list


def test_parse_banned_combinations_file(example_banned_combinations_dict):
    # Assuming the 'test_data' directory is in the same directory as the test module
    file_path = os.path.join(
        os.path.dirname(__file__), "test_data", "banned_combinations.txt"
    )
    result = parse_banned_combinations_file(file_path)
    print(result)
    assert result == example_banned_combinations_dict
