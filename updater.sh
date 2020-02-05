# https://packaging.python.org/tutorials/packaging-projects/
rm -rf ./dist/*
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m twine upload dist/*
