import yaml

from src.validator import validate_input, ValidationError
from .models.asyncapi_3_0_0.AsyncApi3Dot0Dot0SchemaDot import asyncapi_3dot_0dot_0schemadot 


class ParserOptions: 
    def __init__(self, input: dict):
        if 'validate_input' in input:
            self._validate_input: bool = input["validate_input"]
        else:
            self._validate_input: bool = True

    @property
    def validate_input(self):
        return self._validate_input
    @validate_input.setter
    def validate_input(self, validate_input: bool):
        self._validate_input = validate_input


def parse(input: str | dict, options: ParserOptions):
    dict_input: dict
    if isinstance(input, str):
        try:
            dict_input = yaml.safe_load(input)
        except ValueError:
            print("Oops!  That was no valid yaml.  Try again...")
    else:
        dict_input = input
    
    if options.validate_input == True:
        is_valid: bool = validate_input(dict_input)
        if is_valid == False: 
            raise ValidationError("Input is not a valid AsyncAPI document")

    asyncapi_version = input['asyncapi']
    if asyncapi_version == '3.0.0':
        return asyncapi_3dot_0dot_0schemadot(dict_input)


# def parseFromFile(filepath: str): 
#     with open(filepath, 'r') as file:
#         parse(file)