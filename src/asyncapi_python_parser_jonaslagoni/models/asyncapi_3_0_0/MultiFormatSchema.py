from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import MultiFormatSchemaSchemaFormatAnyOf1
from . import MultiFormatSchemaSchemaFormatAnyOf2
class MultiFormatSchema(BaseModel): 
  schema_format: Optional[Union[str, MultiFormatSchemaSchemaFormatAnyOf1.MultiFormatSchemaSchemaFormatAnyOf1, MultiFormatSchemaSchemaFormatAnyOf2.MultiFormatSchemaSchemaFormatAnyOf2]] = Field(description='''A string containing the name of the schema format that is used to define the information. If schemaFormat is missing, it MUST default to application/vnd.aai.asyncapi+json;version={{asyncapi}} where {{asyncapi}} matches the AsyncAPI Version String. In such a case, this would make the Multi Format Schema Object equivalent to the Schema Object. When using Reference Object within the schema, the schemaFormat of the resource being referenced MUST match the schemaFormat of the schema that contains the initial reference. For example, if you reference Avro schema, then schemaFormat of referencing resource and the resource being reference MUST match.''', default=None, alias='''schemaFormat''')
  schema: Optional[Any] = Field(description='''The Multi Format Schema Object represents a schema definition. It differs from the Schema Object in that it supports multiple schema formats or languages (e.g., JSON Schema, Avro, etc.).''', default=None)
  extensions: Optional[dict[str, Any]] = Field(exclude=True, default=None)

  @model_serializer(mode='wrap')
  def custom_serializer(self, handler):
    serialized_self = handler(self)
    extensions = getattr(self, "extensions")
    if extensions is not None:
      for key, value in extensions.items():
        # Never overwrite existing values, to avoid clashes
        if not hasattr(serialized_self, key):
          serialized_self[key] = value

    return serialized_self

  @model_validator(mode='before')
  @classmethod
  def unwrap_extensions(cls, data):
    json_properties = list(data.keys())
    known_object_properties = ['schema_format', 'schema', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['schemaFormat', 'schema', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

