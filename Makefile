
all: docs package
	venv/bin/python3 -m pip freeze > requirements.txt

docs:
	venv/bin/python3 -m pdoc --html --output-dir doc/ src/ --force
	venv/bin/python3 -m pdoc --html --output-dir doc/ tests/ --force

package:
	venv/bin/python3 -m build

install_venv:
	venv/bin/python3 -m pip install -r requirements.txt

