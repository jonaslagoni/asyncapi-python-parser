import unittest
from src.parser import parse, ParserOptions
from src.validator import ValidationError

class TestParser(unittest.TestCase):
    def test_parser_with_no_validation(self):
        """
        Test that we can parse with no validation
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title'}}
        instance = parse(data, ParserOptions({'validate_input': False}))
        
        self.assertEqual('3.0.0', instance.asyncapi)

    def test_parser_throw_exception_with_validation(self):
        """
        Test that we can parse and raise exception on validation problems
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title'}}
        try:
            parse(data, ParserOptions({'validate_input': True}))
            self.fail("Should not succeed")
        except ValidationError as error:
            self.assertIn('ValidationError', type(error).__name__)
        except Exception as error:
            self.fail("Should fail expectedly")


    def test_parser_with_validation(self):
        """
        Test that we can parse valid document with validation
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title', 'version': '1.0.0'}}
        instance = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('3.0.0', instance.asyncapi)

if __name__ == '__main__':
    unittest.main()