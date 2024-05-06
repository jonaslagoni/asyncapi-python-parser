setup: requirements.txt
	pip install -r requirements.txt

test:
	python -m unittest discover ./tests/asyncapi_python_parser_jonaslagoni

generate:
	cd generator && npm i && npm run generate