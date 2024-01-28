import itertools


class MyClass:
    def __init__(
        self,
    ):
        self.students = []
        self.bad_combinations = dict()
        self.min_group_size = 0
        self.n_groups = 1

    def set_min_group_size(self, n):
        self.min_group_size = n

    def set_n_groups(self, n):
        self.n_groups = n

    def __str__(self):
        return str(vars(self))

    def add_students(self, list_of_students):
        self.students += list_of_students

    def update_bad_combinations(self, combos_to_add: dict):
        self.bad_combinations.update(combos_to_add)

    def find_valid_groups(self):
        all_possible_groupings = self._generate_all_possible_groupings()
        groupings_over_min_size = self._remove_groups_under_min_size(
            all_possible_groupings
        )
        if self.bad_combinations:
            return self._remove_bad_combinations(groupings_over_min_size)
        else:
            return groupings_over_min_size

    def _is_valid_grouping(self, input_group):
        for subgroup in input_group:
            for student in self.bad_combinations.keys():
                if student in subgroup:
                    blacklist = self.bad_combinations[student]
                    other_students_in_subgroup = subgroup - {student}
                    for other_student in other_students_in_subgroup:
                        if other_student in blacklist:
                            return False
        return True

    def _remove_bad_combinations(self, group_configuration):
        valid_groupings = []
        for g in group_configuration:
            if self._is_valid_grouping(g):
                valid_groupings.append(g)

        return set(valid_groupings)

    def _remove_groups_under_min_size(
        self,
        groups,
    ):
        return set(g for g in groups if len(min(g, key=len)) >= self.min_group_size)

    def _generate_all_possible_groupings(self):
        # Generate all combinations of distributing elements into n_groups groups
        all_possible_groupings = []

        for distribution in itertools.product(
            range(self.n_groups), repeat=len(self.students)
        ):
            groups = [[] for _ in range(self.n_groups)]

            for student, group_index in zip(self.students, distribution):
                groups[group_index].append(student)

            groups = frozenset(map(frozenset, groups))
            all_possible_groupings.append(groups)
        return set(all_possible_groupings)

    def print_solution_nicely(self, solutions):
        for i, solution in enumerate(solutions):
            print(f"===== Solution {i+1} ===== ")
            for j, grp in enumerate(solution):
                print(f"Group {j+1}:")
                for student in grp:
                    print(f"\t {student}")
