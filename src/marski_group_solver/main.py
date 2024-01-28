from marski_group_solver.input_parser import get_inputs, parse_input_args


def main():
    args = parse_input_args()
    student_register, banned_combinations = get_inputs(
        args.student_register_filepath,
        args.bad_combinations_filepath,
    )
    print(student_register)
    print(banned_combinations)


if __name__ == "__main__":
    main()
