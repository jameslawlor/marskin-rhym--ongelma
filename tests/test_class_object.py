from marski_group_solver.my_class import MyClass


def test_class_init():
    my_class = MyClass()
    assert my_class.students == []
    assert my_class.bad_combinations == dict()


def test_class_add_students(example_students_list):
    my_class = MyClass()
    my_class.add_students(example_students_list)
    assert my_class.students == example_students_list


def test_update_bad_combinations(example_banned_combinations_dict):
    my_class = MyClass()
    my_class.update_bad_combinations(example_banned_combinations_dict)
    assert my_class.bad_combinations == example_banned_combinations_dict


# def test_find_valid_groups(example_students_list, example_banned_combinations_dict):
#     my_class = MyClass()
#     my_class.add_students(example_students_list)
#     my_class.update_bad_combinations(example_banned_combinations_dict)
#     assert my_class.find_valid_groups(n_groups=2) == [
#         [["Student1", "Student4"], ["Student2", "Student3"]]
#     ]


def test__generate_all_possible_groupings(example_groupings):
    my_class = MyClass()
    my_class.add_students(["Student1", "Student2"])
    groupings = my_class._generate_all_possible_groupings(n_groups=2)
    assert groupings == example_groupings


def test__remove_groups_under_min_size(example_groupings):
    my_class = MyClass()
    result = my_class._remove_groups_under_min_size(example_groupings, min_size=1)
    assert result == {
        frozenset(
            {
                frozenset({"Student1"}),
                frozenset({"Student2"}),
            }
        )
    }


def test__remove_bad_combinations():
    input_groups = {
        frozenset(
            {
                frozenset({"Student1", "Student2"}),
                frozenset({"Student3", "Student4"}),
            }
        ),
        frozenset(
            {
                frozenset({"Student1", "Student4"}),
                frozenset({"Student2", "Student3"}),
            }
        ),
        frozenset(
            {
                frozenset({"Student1", "Student3"}),
                frozenset({"Student2", "Student4"}),
            }
        ),
    }

    my_class = MyClass()
    my_class.update_bad_combinations({"Student1": ["Student2", "Student3"]})
    result = my_class._remove_bad_combinations(input_groups)

    assert result == {
        frozenset(
            {
                frozenset({"Student1", "Student4"}),
                frozenset({"Student2", "Student3"}),
            }
        )
    }
