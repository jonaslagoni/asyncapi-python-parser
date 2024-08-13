from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import JsonSchemaDraft07Schema
from . import Xml
from . import ExternalDocs
class Schema(BaseModel): 
  dollar_ref: Optional[str] = Field(default=None, alias='''$ref''')
  format: Optional[str] = Field(default=None)
  title: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  description: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  default: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  multiple_of: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''multipleOf''')
  maximum: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  exclusive_maximum: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''exclusiveMaximum''')
  minimum: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  exclusive_minimum: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''exclusiveMinimum''')
  max_length: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''maxLength''')
  min_length: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''minLength''')
  pattern: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  max_items: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''maxItems''')
  min_items: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''minItems''')
  unique_items: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''uniqueItems''')
  max_properties: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''maxProperties''')
  min_properties: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None, alias='''minProperties''')
  required: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  enum: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  additional_properties: Optional[Union[Schema, bool]] = Field(default=None, alias='''additionalProperties''')
  type: Optional[JsonSchemaDraft07Schema.JsonSchemaDraft07Schema] = Field(description='''Core schema meta-schema''', default=None)
  items: Optional[Union[Schema, List[Schema]]] = Field(default=None)
  all_of: Optional[List[Schema]] = Field(default=None, alias='''allOf''')
  properties: Optional[dict[str, Schema]] = Field(default=None)
  discriminator: Optional[str] = Field(default=None)
  read_only: Optional[bool] = Field(default=None, alias='''readOnly''')
  xml: Optional[Xml.Xml] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''information about external documentation''', default=None, alias='''externalDocs''')
  example: Optional[Any] = Field(default=None)
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
    known_object_properties = ['dollar_ref', 'format', 'title', 'description', 'default', 'multiple_of', 'maximum', 'exclusive_maximum', 'minimum', 'exclusive_minimum', 'max_length', 'min_length', 'pattern', 'max_items', 'min_items', 'unique_items', 'max_properties', 'min_properties', 'required', 'enum', 'additional_properties', 'type', 'items', 'all_of', 'properties', 'discriminator', 'read_only', 'xml', 'external_docs', 'example', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['$ref', 'format', 'title', 'description', 'default', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'maxProperties', 'minProperties', 'required', 'enum', 'additionalProperties', 'type', 'items', 'allOf', 'properties', 'discriminator', 'readOnly', 'xml', 'externalDocs', 'example', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

