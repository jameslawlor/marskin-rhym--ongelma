import pytest


@pytest.fixture
def example_students_list():
    return [
        "Student1",
        "Student2",
        "Student3",
        "Student4",
    ]


@pytest.fixture
def example_banned_combinations_dict():
    return {"Student1": ["Student2", "Student3"]}


@pytest.fixture
def example_groupings():
    return {
        frozenset({frozenset({"Student2"}), frozenset({"Student1"})}),
        frozenset({frozenset(), frozenset({"Student1", "Student2"})}),
    }
