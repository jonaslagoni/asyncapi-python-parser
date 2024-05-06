import unittest
from src.asyncapi_python_parser_jonaslagoni.parser import parse, ParserOptions, ValidationError
from os import listdir
from os.path import isfile, join
import json

class TestDocuments(unittest.TestCase):
    def test_all_3_0_0_example_docs(self):
        """
        Test that all 3.0.0 documents can be validated and parsed
        """

        directory_path = "./tests/docs/3.0.0"
        document_files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
        for f in document_files:
            full_path_to_document = join(directory_path, f)
            with open(full_path_to_document, 'r') as f2:
                document = json.load(f2)
            instance = parse(document, ParserOptions({'validate_input': False}))
            self.assertEqual('3.0.0', instance.asyncapi)

if __name__ == '__main__':
    unittest.main()