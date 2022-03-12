black: ## Black format every python file to line length 100
	find . -type f -name "*.py" | xargs black --line-length=100;
	find . -type f -name "*.py" | xargs absolufy-imports;
	make clean;

flake: ## Flake8 every python file
	find . -type f -name "*.py" -a | xargs flake8;

pylint: ## pylint every python file
	find . -type f -name "*.py" -a | xargs pylint;

unittest: ## Verbosely test ./tests/test_natlparks.py
	python tests/test_natlparks.py;
	make clean;

pre-commit: ## Install and autoupdate pre-commit
	pre-commit install;
	pre-commit autoupdate;

build: ## Build package distribution files
	python setup.py sdist bdist_wheel;

publish: ## Publish package distribution files to pypi
	twine upload dist/*;
	make clean;

clean: ## Remove package distribution files and pycache
	rm -rf *.egg-info ./dist ./build;
	find . -type d -name "__pycache__" | xargs rm -r;
