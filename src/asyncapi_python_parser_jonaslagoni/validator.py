import json
import traceback
from jsonschema import validate, exceptions

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_schema_file(asyncapi_version: str):
    full_path_to_document = f"./generator/definitions/{asyncapi_version}-without-$id.json"
    with open(full_path_to_document, 'r') as f:
        schema = json.load(f)
    return schema

def validate_input(input: dict):
    asyncapi_version = input['asyncapi']
    try:
        json_schema_file = get_schema_file(asyncapi_version)
        validate(instance=input, schema=json_schema_file)
        return True
    except exceptions.SchemaError:
        print("Schema error")
        print(traceback.format_exc())
        return False
    except exceptions.ValidationError:
        print("Validation error")
        print(traceback.format_exc())
        return False
