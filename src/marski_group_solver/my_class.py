import itertools


class MyClass:
    def __init__(
        self,
    ):
        self.students = []
        self.bad_combinations = dict()

    def __str__(self):
        return vars(self)

    def add_students(self, list_of_students):
        self.students += list_of_students

    def update_bad_combinations(self, combos_to_add: dict):
        self.bad_combinations.update(combos_to_add)

    def find_valid_groups(self, n_groups):
        valid_groupings = {}
        all_possible_groupings = self._generate_all_possible_groupings(n_groups)
        groupings_over_min_size = self._remove_groups_under_min_size(
            all_possible_groupings
        )
        deduped = self._remove_duplicate_groupings(groupings_over_min_size)
        if self.bad_combinations:
            return self._remove_bad_combinations(deduped)
        else:
            return deduped

    def _is_valid_grouping(self, input_group):
        print(self.bad_combinations)

        # for subgroup in g:
        #     for student in self.bad_combinations.keys():
        #         print(student, subgroup, self.bad_combinations.keys())
        #         if student in subgroup:
        #             print(f"Found student {student} in group {subgroup}")

        return True

    def _remove_bad_combinations(self, group_configuration):
        valid_groupings = []
        for g in group_configuration:
            if self._is_valid_grouping(g):
                valid_groupings.append(g)

        return set(valid_groupings)

    def _remove_groups_under_min_size(self, groups, min_size=2):
        return set(g for g in groups if len(min(g, key=len)) >= min_size)

    def _generate_all_possible_groupings(self, n_groups):
        # Generate all combinations of distributing elements into n_groups groups
        all_possible_groupings = []
        for distribution in itertools.product(
            range(n_groups), repeat=len(self.students)
        ):
            groups = [[] for _ in range(n_groups)]

            for student, group_index in zip(self.students, distribution):
                groups[group_index].append(student)

            groups = frozenset(map(frozenset, groups))
            all_possible_groupings.append(groups)

        return set(all_possible_groupings)
