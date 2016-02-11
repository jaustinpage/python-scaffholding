deps:
	virtualenv env
	pip install -r requirements.txt
	
	echo "Run source env/bin/activate"

clean:
	pyclean .

lint:
	pep8 --show-source --show-pep8 ./*.py

freeze:
	pip freeze > requirements.txt

unittest:
	python -m unittest discover -s unit_tests -p "*_test.py"

init: deps clean
