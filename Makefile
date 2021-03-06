.PHONY: clean	clean-build clean-pyc docs help

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test: clean
	pytest --flake8

docs:
	rm -f docs/discriminate_agkistrodon.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ discriminate_agkistrodon
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

install: test
	python setup.py install

uninstall:
	pip uninstall discriminate_agkistrodon

docserver:
	cd docs/_build/html && python -m SimpleHTTPServer 9000