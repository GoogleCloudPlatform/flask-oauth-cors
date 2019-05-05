init:
	python3 -m pip install --user -r requirements.txt

package:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

docs:
	cd docs && sphinx-build -M html . .

.PHONY: init package docs
