from __future__ import annotations
from src.asyncapi_python_parser_jonaslagoni.models.asyncapi_3_0_0.AsyncApi3x0x0Schemax import AsyncApi3x0x0Schemax
import unittest

class ModelTesting(unittest.TestCase):
  def test_should_be_able_to_serialize_extensions(self):
    """
    We should be able to serialize and de-serialize AsyncAPI documents with custom extensions. 
    """
    data = {'asyncapi': '3.0.0', "x-test": "test"}
    instance = AsyncApi3x0x0Schemax(**data)
    json_data = instance.model_dump_json(by_alias=True)
    instance2 = AsyncApi3x0x0Schemax.model_validate_json(json_data)
    json_data2 = instance2.model_dump_json(by_alias=True)

    self.assertEqual('', json_data)
    self.assertEqual(json_data, json_data2)
    
  def test_should_be_able_to_serialize_unions(self):
    """
    We should be able to serialize and de-serialize AsyncAPI documents with unions. 
    """
    data = {'asyncapi': '3.0.0', "channels": {"test": {"$ref": "test"}}}
    instance = AsyncApi3x0x0Schemax(**data)
    json_data = instance.model_dump_json(by_alias=True)
    instance2 = AsyncApi3x0x0Schemax.model_validate_json(json_data)
    json_data2 = instance2.model_dump_json(by_alias=True)

    self.assertEqual('', json_data)
    self.assertEqual(json_data, json_data2)

  def test_should_be_able_to_serialize_unions_2(self):
    """
    We should be able to serialize and de-serialize AsyncAPI documents with unions 2. 
    """
    data = {'asyncapi': '3.0.0', "channels": {"test": {"description": "test"}}}
    instance = AsyncApi3x0x0Schemax(**data)
    json_data = instance.model_dump_json(by_alias=True)
    instance2 = AsyncApi3x0x0Schemax.model_validate_json(json_data)
    json_data2 = instance2.model_dump_json(by_alias=True)

    self.assertEqual('', json_data)
    self.assertEqual(json_data, json_data2)

if __name__ == '__main__':
    unittest.main()