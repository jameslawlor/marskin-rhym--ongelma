import argparse


def parse_all_students_file(path):
    """
    TODO:
        - Check unique naming
    """
    with open(path, "r") as input_file:
        return [line.rstrip("\n") for line in input_file]


def parse_banned_combinations_file(path):
    """
    TODO:
        - Assertion error when duplicates in student_name
    """
    banned_combinations_dict = {}
    with open(path, "r") as input_file:
        for line in input_file:
            parts = line.split(":")
            student_name = parts[0].strip()
            connected_students = [s.strip() for s in parts[1].split(",")]
            banned_combinations_dict[student_name] = connected_students
    return banned_combinations_dict


def parse_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--student_register_filepath",
    )
    # TODO: Make optional
    parser.add_argument(
        "--banned_combinations_filepath",
    )
    args = parser.parse_args()
    return args
