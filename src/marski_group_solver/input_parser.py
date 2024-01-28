import argparse


def get_inputs(student_register_filepath, bad_combinations_filepath):
    register = read_file(student_register_filepath)
    if bad_combinations_filepath:
        bad_combinations = parse_bad_combinations_file(bad_combinations_filepath)
    else:
        bad_combinations = None
    return register, bad_combinations


def read_file(path):
    with open(path, "r") as input_file:
        data = [line.rstrip("\n") for line in input_file]
    return data


def parse_bad_combinations_file(path) -> dict:
    bad_combos_dict = {}
    data = read_file(path)
    for line in data:
        parts = line.split(":")
        student_name = parts[0].strip()
        connected_students = [s.strip() for s in parts[1].split(",")]
        if student_name not in bad_combos_dict.keys():
            bad_combos_dict[student_name] = connected_students
        else:
            raise ValueError(
                f"student_name {student_name} already in banned combinations keys! Check inputs!"
            )
    return bad_combos_dict


def parse_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--student_register_filepath",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--bad_combinations_filepath",
        type=str,
        required=False,
        default=None,
    )
    return parser.parse_args()
