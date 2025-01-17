from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import JsonSchemaDraft07SchemaSimpleTypes
class CoreSchemaMetaSchemaObject(BaseModel): 
  dollar_id: Optional[str] = Field(default=None, alias='''$id''')
  dollar_schema: Optional[str] = Field(default=None, alias='''$schema''')
  dollar_ref: Optional[str] = Field(default=None, alias='''$ref''')
  dollar_comment: Optional[str] = Field(default=None, alias='''$comment''')
  title: Optional[str] = Field(default=None)
  description: Optional[str] = Field(default=None)
  default: Optional[Any] = Field(default=None)
  read_only: Optional[bool] = Field(default=None, alias='''readOnly''')
  write_only: Optional[bool] = Field(default=None, alias='''writeOnly''')
  examples: Optional[List[Any]] = Field(default=None)
  multiple_of: Optional[float] = Field(default=None, alias='''multipleOf''')
  maximum: Optional[float] = Field(default=None)
  exclusive_maximum: Optional[float] = Field(default=None, alias='''exclusiveMaximum''')
  minimum: Optional[float] = Field(default=None)
  exclusive_minimum: Optional[float] = Field(default=None, alias='''exclusiveMinimum''')
  max_length: Optional[int] = Field(default=None, alias='''maxLength''')
  min_length: Optional[int] = Field(default=None, alias='''minLength''')
  pattern: Optional[str] = Field(default=None)
  additional_items: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''additionalItems''')
  items: Optional[Union[CoreSchemaMetaSchemaObject | bool, List[CoreSchemaMetaSchemaObject | bool]]] = Field(default=None)
  max_items: Optional[int] = Field(default=None, alias='''maxItems''')
  min_items: Optional[int] = Field(default=None, alias='''minItems''')
  unique_items: Optional[bool] = Field(default=None, alias='''uniqueItems''')
  contains: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None)
  max_properties: Optional[int] = Field(default=None, alias='''maxProperties''')
  min_properties: Optional[int] = Field(default=None, alias='''minProperties''')
  required: Optional[List[str]] = Field(default=None)
  additional_properties: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''additionalProperties''')
  definitions: Optional[dict[str, CoreSchemaMetaSchemaObject | bool]] = Field(default=None)
  properties: Optional[dict[str, CoreSchemaMetaSchemaObject | bool]] = Field(default=None)
  pattern_properties: Optional[dict[str, CoreSchemaMetaSchemaObject | bool]] = Field(default=None, alias='''patternProperties''')
  dependencies: Optional[dict[str, CoreSchemaMetaSchemaObject | bool | List[str]]] = Field(default=None)
  property_names: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''propertyNames''')
  const: Optional[Any] = Field(default=None)
  enum: Optional[List[Any]] = Field(default=None)
  type: Optional[Union[JsonSchemaDraft07SchemaSimpleTypes.JsonSchemaDraft07SchemaSimpleTypes, List[JsonSchemaDraft07SchemaSimpleTypes.JsonSchemaDraft07SchemaSimpleTypes]]] = Field(default=None)
  format: Optional[str] = Field(default=None)
  content_media_type: Optional[str] = Field(default=None, alias='''contentMediaType''')
  content_encoding: Optional[str] = Field(default=None, alias='''contentEncoding''')
  reserved_if: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''if''')
  then: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None)
  reserved_else: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''else''')
  all_of: Optional[List[CoreSchemaMetaSchemaObject | bool]] = Field(default=None, alias='''allOf''')
  any_of: Optional[List[CoreSchemaMetaSchemaObject | bool]] = Field(default=None, alias='''anyOf''')
  one_of: Optional[List[CoreSchemaMetaSchemaObject | bool]] = Field(default=None, alias='''oneOf''')
  reserved_not: Optional[Union[CoreSchemaMetaSchemaObject, bool]] = Field(default=None, alias='''not''')
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
    known_object_properties = ['dollar_id', 'dollar_schema', 'dollar_ref', 'dollar_comment', 'title', 'description', 'default', 'read_only', 'write_only', 'examples', 'multiple_of', 'maximum', 'exclusive_maximum', 'minimum', 'exclusive_minimum', 'max_length', 'min_length', 'pattern', 'additional_items', 'items', 'max_items', 'min_items', 'unique_items', 'contains', 'max_properties', 'min_properties', 'required', 'additional_properties', 'definitions', 'properties', 'pattern_properties', 'dependencies', 'property_names', 'const', 'enum', 'type', 'format', 'content_media_type', 'content_encoding', 'reserved_if', 'then', 'reserved_else', 'all_of', 'any_of', 'one_of', 'reserved_not', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['$id', '$schema', '$ref', '$comment', 'title', 'description', 'default', 'readOnly', 'writeOnly', 'examples', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'additionalItems', 'items', 'maxItems', 'minItems', 'uniqueItems', 'contains', 'maxProperties', 'minProperties', 'required', 'additionalProperties', 'definitions', 'properties', 'patternProperties', 'dependencies', 'propertyNames', 'const', 'enum', 'type', 'format', 'contentMediaType', 'contentEncoding', 'if', 'then', 'else', 'allOf', 'anyOf', 'oneOf', 'not', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

