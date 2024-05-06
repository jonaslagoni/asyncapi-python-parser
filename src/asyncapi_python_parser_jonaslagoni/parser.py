import yaml
from jsonschema import RefResolver
from .validator import validate_input, ValidationError
from .traits import apply_traits
from .models.asyncapi_3_0_0.AsyncApi3Dot0Dot0SchemaDot import AsyncApi3Dot0Dot0SchemaDot 
from .models.asyncapi_2_6_0.AsyncApi2Dot6Dot0SchemaDot import AsyncApi2Dot6Dot0SchemaDot 
from .models.asyncapi_2_5_0.AsyncApi2Dot5Dot0SchemaDot import AsyncApi2Dot5Dot0SchemaDot 
from .models.asyncapi_2_4_0.AsyncApi2Dot4Dot0SchemaDot import AsyncApi2Dot4Dot0SchemaDot 
from .models.asyncapi_2_3_0.AsyncApi2Dot3Dot0SchemaDot import AsyncApi2Dot3Dot0SchemaDot 
from .models.asyncapi_2_2_0.AsyncApi2Dot2Dot0SchemaDot import AsyncApi2Dot2Dot0SchemaDot 
from .models.asyncapi_2_1_0.AsyncApi2Dot1Dot0SchemaDot import AsyncApi2Dot1Dot0SchemaDot 
from .models.asyncapi_2_0_0.AsyncApi2Dot0Dot0SchemaDot import AsyncApi2Dot0Dot0SchemaDot 

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
        return AsyncApi3Dot0Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.6.0':
        return AsyncApi2Dot6Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.5.0':
        return AsyncApi2Dot5Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.4.0':
        return AsyncApi2Dot4Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.3.0':
        return AsyncApi2Dot3Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.2.0':
        return AsyncApi2Dot2Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.1.0':
        return AsyncApi2Dot1Dot0SchemaDot(dict_input)
    if asyncapi_version == '2.0.0':
        return AsyncApi2Dot0Dot0SchemaDot(dict_input)

def parse_from_file(filepath: str, options: ParserOptions): 
    with open(filepath, 'r') as file:
        parse(file.read(), options)