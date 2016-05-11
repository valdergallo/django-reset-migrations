help:
	@echo "register		send package to pypi"

register:
	python setup.py build bdist_wheel bdist upload register
