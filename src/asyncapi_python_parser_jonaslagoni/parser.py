import yaml
from jsonschema import RefResolver
from .validator import validate_input, ValidationError
from .traits import apply_traits
from .models.asyncapi_3_0_0.AsyncApi3x0x0Schemax import AsyncApi3x0x0Schemax 
from .models.asyncapi_2_6_0.AsyncApi2x6x0Schemax import AsyncApi2x6x0Schemax 
from .models.asyncapi_2_5_0.AsyncApi2x5x0Schemax import AsyncApi2x5x0Schemax 
from .models.asyncapi_2_4_0.AsyncApi2x4x0Schemax import AsyncApi2x4x0Schemax 
from .models.asyncapi_2_3_0.AsyncApi2x3x0Schemax import AsyncApi2x3x0Schemax 
from .models.asyncapi_2_2_0.AsyncApi2x2x0Schemax import AsyncApi2x2x0Schemax 
from .models.asyncapi_2_1_0.AsyncApi2x1x0Schemax import AsyncApi2x1x0Schemax 
from .models.asyncapi_2_0_0.AsyncApi2x0x0Schemax import AsyncApi2x0x0Schemax 

class ParserOptions: 
    def __init__(self, input: dict):
        if 'validate_input' in input:
            self._validate_input: bool = input["validate_input"]
        else:
            self._validate_input: bool = True
        if 'apply_traits' in input:
            self._apply_traits: bool = input["apply_traits"]
        else:
            self._apply_traits: bool = True
        if 'resolve_references' in input:
            self._resolve_references: bool = input["resolve_references"]
        else:
            self._resolve_references: bool = True

    @property
    def validate_input(self):
        return self._validate_input

    @property
    def apply_traits(self):
        return self._apply_traits

    @property
    def resolve_references(self):
        return self._resolve_references

def parse(input: str | dict, options: ParserOptions):
    dict_input: dict
    if isinstance(input, str):
        try:
            dict_input = yaml.safe_load(input)
        except ValueError:
            print("Oops!  That was no valid yaml.  Try again...")
    else:
        dict_input = input

    if options.resolve_references == True:
        resolver = RefResolver('', dict_input)
    
    if options.validate_input == True:
        is_valid: bool = validate_input(dict_input)
        if is_valid == False: 
            raise ValidationError("Input is not a valid AsyncAPI document")

    if options.apply_traits == True:
        apply_traits(dict_input)

    asyncapi_version = input['asyncapi']
    if asyncapi_version == '3.0.0':
        return AsyncApi3x0x0Schemax(dict_input)
    if asyncapi_version == '2.6.0':
        return AsyncApi2x6x0Schemax(dict_input)
    if asyncapi_version == '2.5.0':
        return AsyncApi2x5x0Schemax(dict_input)
    if asyncapi_version == '2.4.0':
        return AsyncApi2x4x0Schemax(dict_input)
    if asyncapi_version == '2.3.0':
        return AsyncApi2x3x0Schemax(dict_input)
    if asyncapi_version == '2.2.0':
        return AsyncApi2x2x0Schemax(dict_input)
    if asyncapi_version == '2.1.0':
        return AsyncApi2x1x0Schemax(dict_input)
    if asyncapi_version == '2.0.0':
        return AsyncApi2x0x0Schemax(dict_input)

def parse_from_file(filepath: str, options: ParserOptions): 
    with open(filepath, 'r') as file:
        parse(file.read(), options)