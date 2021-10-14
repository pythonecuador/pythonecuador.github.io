clean:
	rm -rf cache output .doit.db .doit.db.*

serve:
	nikola auto

deploy:
	NIKOLA_DEPLOY=python.ec nikola github_deploy

lint:
	python -m nox -r -s lint_python

format:
	python -m nox -r -s format_python

.PHONY: clean serve
