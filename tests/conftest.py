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
