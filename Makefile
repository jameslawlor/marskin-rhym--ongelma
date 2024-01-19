.PHONY: all clean ruff test solve_example 

# Default target
all: ruff test solutions clean

# Clean temporary and generated files
clean:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf

ruff:
	ruff format .
	ruff check .

# Run tests
test:
	pytest -vs

solve_example:
	python src/marski-group-solver/main.py --student_register_filepath inputs/example_class/all_students.txt --banned_combinations_filepath inputs/example_class/banned_combinations.txt