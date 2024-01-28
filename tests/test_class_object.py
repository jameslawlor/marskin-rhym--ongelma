import pytest
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


def test_find_valid_groups(
    example_students_list, example_banned_combinations_dict, expected_solution
):
    my_class = MyClass()
    my_class.add_students(example_students_list)
    my_class.update_bad_combinations(example_banned_combinations_dict)
    my_class.set_n_groups(2)
    my_class.set_min_group_size(2)
    result = my_class.find_valid_groups()
    assert result == expected_solution


def test__generate_all_possible_groupings(example_groupings):
    my_class = MyClass()
    my_class.add_students(["Student1", "Student2"])
    my_class.set_n_groups(2)
    groupings = my_class._generate_all_possible_groupings()
    assert groupings == example_groupings


def test__remove_groups_under_min_size(example_groupings):
    my_class = MyClass()
    my_class.set_min_group_size(1)
    result = my_class._remove_groups_under_min_size(example_groupings)
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


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            frozenset(
                {
                    frozenset({"Student1", "Student4"}),
                    frozenset({"Student2", "Student3"}),
                }
            ),
            True,
        ),
        (
            frozenset(
                {
                    frozenset({"Student1", "Student2"}),
                    frozenset({"Student3", "Student4"}),
                }
            ),
            False,
        ),
    ],
)
def test__is_valid_grouping(test_input, expected):
    my_class = MyClass()
    my_class.update_bad_combinations({"Student1": ["Student2", "Student3"]})
    result = my_class._is_valid_grouping(test_input)
    assert result == expected
