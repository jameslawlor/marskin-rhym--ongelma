import itertools
from input_parser import (
    parse_input_args,
    parse_all_students_file,
    parse_banned_combinations_file,
)


class StudentGroups:
    def __init__(self, list_of_students=[]):
        self.students = list_of_students
        self.banned_combinations = {}
        self.n_students = len(list_of_students)
        self.min_group_size = None

    def __str__(self):
        return (
            f"\n == Class attributes == \n"
            f"students: {self.students} \n"
            f"banned_combinations: {self.banned_combinations} \n"
            f"n_students: {self.n_students} \n"
        )

    def assign_groups(self, desired_group_size=2):
        self.desired_group_size = desired_group_size

        all_combinations = []

        # Generate combinations for each group size
        print(itertools.batched(self.students))
        stop
        # all_combinations = list(set(itertools.permutations(self.students, desired_group_size)))

        # print(all_combinations)
        # Filter out disallowed combinations

        allowed_combinations = all_combinations
        # allowed_combinations = [
        #     combo
        #     for combo in all_combinations
        #     if all(student not in self.banned_combinations for student in combo)
        # ]

        return allowed_combinations


def main():
    args = parse_input_args()
    student_register = parse_all_students_file(args.student_register_filepath)
    my_class = StudentGroups(student_register)
    print(my_class)

    if args.banned_combinations_filepath:
        my_class.banned_combinations = parse_banned_combinations_file(
            args.banned_combinations_filepath
        )

    result = my_class.assign_groups()

    if result:
        print("Possible group configurations:")
        for group in result:
            print(group)
    else:
        print("No result!")


if __name__ == "__main__":
    main()
