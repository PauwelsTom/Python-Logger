# Nom du package (à adapter si besoin)
PACKAGE = logger_pauwels

# Variable VERSION optionnelle
VERSION ?=

build_local:
	python -m build
ifeq ($(VERSION),)
    # Pas de version donnée → on prend le dernier wheel
	pip install --force-reinstall $$(ls -t dist/$(PACKAGE)-*.whl | head -n1)
else
    # Version donnée → on installe ce fichier précis
	pip install --force-reinstall dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl
endif

publish:
	python -m build
	twine upload dist/*

test:
	python tests/main_test.py