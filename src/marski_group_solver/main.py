from marski_group_solver.input_parser import get_inputs, parse_input_args
from marski_group_solver.my_class import MyClass


def main():
    args = parse_input_args()
    student_register, banned_combinations = get_inputs(
        args.student_register_filepath,
        args.bad_combinations_filepath,
    )
    my_class = MyClass()
    my_class.add_students(student_register)
    my_class.update_bad_combinations(banned_combinations)

    my_class.set_min_group_size(2)
    my_class.set_n_groups(2)

    solutions = my_class.find_valid_groups()
    my_class.print_solution_nicely(solutions)


if __name__ == "__main__":
    main()
