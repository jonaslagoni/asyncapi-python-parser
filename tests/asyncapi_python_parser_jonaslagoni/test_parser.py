import unittest
from src.asyncapi_python_parser_jonaslagoni.parser import parse, ParserOptions
from src.asyncapi_python_parser_jonaslagoni.validator import ValidationError
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_3_0_0.AsyncApi3x0x0Schemax import AsyncApi3x0x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_6_0.AsyncApi2x6x0Schemax import AsyncApi2x6x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_5_0.AsyncApi2x5x0Schemax import AsyncApi2x5x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_4_0.AsyncApi2x4x0Schemax import AsyncApi2x4x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_3_0.AsyncApi2x3x0Schemax import AsyncApi2x3x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_2_0.AsyncApi2x2x0Schemax import AsyncApi2x2x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_1_0.AsyncApi2x1x0Schemax import AsyncApi2x1x0Schemax 
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_2_0_0.AsyncApi2x0x0Schemax import AsyncApi2x0x0Schemax 

class TestParser(unittest.TestCase):
    def test_parser_with_no_validation(self):
        """
        Test that we can parse with no validation
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title', 'version': '1.0.0', 'someNonExisting_value': 'test'}}
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
            self.fail("Should fail expectedly" + type(error).__name__)


    def test_parser_with_validation(self):
        """
        Test that we can parse valid document with validation
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title', 'version': '1.0.0'}}
        instance: AsyncApi3x0x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('3.0.0', instance.asyncapi)

    def test_parser_with_default_options(self):
        """
        Test that we can parse with default options
        """

        data = {'asyncapi': '3.0.0', 'info': {'title': 'test title', 'version': '1.0.0'}}
        instance: AsyncApi3x0x0Schemax = parse(data)
        self.assertEqual('3.0.0', instance.asyncapi)

    def test_parser_with_asyncapi_2_6_0(self):
        """
        Test that we can parse valid AsyncAPI 2.6.0 document
        """

        data = {'asyncapi': '2.6.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x6x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.6.0', instance.asyncapi.value)

    def test_parser_with_asyncapi_2_5_0(self):
        """
        Test that we can parse valid AsyncAPI 2.5.0 document
        """

        data = {'asyncapi': '2.5.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x5x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.5.0', instance.asyncapi.value)

    def test_parser_with_asyncapi_2_4_0(self):
        """
        Test that we can parse valid AsyncAPI 2.4.0 document
        """

        data = {'asyncapi': '2.4.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x4x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.4.0', instance.asyncapi.value)

    def test_parser_with_asyncapi_2_3_0(self):
        """
        Test that we can parse valid AsyncAPI 2.3.0 document
        """

        data = {'asyncapi': '2.3.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x3x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.3.0', instance.asyncapi.value)


    def test_parser_with_asyncapi_2_2_0(self):
        """
        Test that we can parse valid AsyncAPI 2.2.0 document
        """

        data = {'asyncapi': '2.2.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x2x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.2.0', instance.asyncapi.value)

    def test_parser_with_asyncapi_2_1_0(self):
        """
        Test that we can parse valid AsyncAPI 2.1.0 document
        """

        data = {'asyncapi': '2.1.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x1x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.1.0', instance.asyncapi.value)


    def test_parser_with_asyncapi_2_0_0(self):
        """
        Test that we can parse valid AsyncAPI 2.0.0 document
        """

        data = {'asyncapi': '2.0.0', 'info': {'title': 'test title', 'version': '1.0.0'}, 'channels': {}}
        instance: AsyncApi2x0x0Schemax = parse(data, ParserOptions({'validate_input': True}))
        self.assertEqual('2.0.0', instance.asyncapi.value)
if __name__ == '__main__':
    unittest.main()