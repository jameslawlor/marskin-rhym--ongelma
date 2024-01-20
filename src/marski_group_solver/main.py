import itertools
import math
from marski_group_solver.input_parser import (
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

    def assign_groups(self, min_group_size=2):
        self.n_groups = math.ceil(self.n_students / min_group_size)
        all_distributions = []

        # Generate all combinations of distributing elements into two groups
        for distribution in itertools.product(
            range(self.n_groups), repeat=len(self.students)
        ):
            groups = [[] for _ in range(self.n_groups)]

            for student, group_index in zip(self.students, distribution):
                groups[group_index].append(student)

            all_distributions.append(tuple(map(frozenset,groups)))


        # Groups must be min_group_size or larger
        pruned_groupings = tuple([g for g in all_distributions if len(min(g,key=len)) >= min_group_size])

        # convert to set to remove duplicates
        no_dupes = set(map(frozenset,pruned_groupings))
        # convert all back to tuples
        # unique_groupings = []
        # for _ in no_dupes:
        #     unique_groupings.append(tuple([tuple(x) for x in _]))

        # print(unique_groupings)
        # Filter out disallowed combinations
        allowed_groups = []

        for g in no_dupes:
            for subgroup in g:
                if 

        # allowed_groups = all_permutations
        # allowed_combinations = [
        #     combo
        #     for combo in all_combinations
        #     if all(student not in self.banned_combinations for student in combo)
        # ]

        return allowed_groups


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
