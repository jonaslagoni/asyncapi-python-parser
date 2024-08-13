from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import CoreSchemaMetaSchemaObject
from . import JsonSchemaDraft07SchemaType
from . import SchemaAllOf1DiscriminatorObject
from . import ExternalDocs
from . import OpenapiSchema30Xml
class MessageOneOf1OneOf1PayloadObject(BaseModel): 
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
  exclusive_maximum: Optional[Union[float, bool]] = Field(default=None, alias='''exclusiveMaximum''')
  minimum: Optional[float] = Field(default=None)
  exclusive_minimum: Optional[Union[float, bool]] = Field(default=None, alias='''exclusiveMinimum''')
  max_length: Optional[int] = Field(default=None, alias='''maxLength''')
  min_length: Optional[int] = Field(default=None, alias='''minLength''')
  pattern: Optional[str] = Field(default=None)
  additional_items: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''additionalItems''')
  items: Optional[Union[CoreSchemaMetaSchemaObject.CoreSchemaMetaSchemaObject | bool, List[MessageOneOf1OneOf1PayloadObject | bool]]] = Field(default=None)
  max_items: Optional[int] = Field(default=None, alias='''maxItems''')
  min_items: Optional[int] = Field(default=None, alias='''minItems''')
  unique_items: Optional[bool] = Field(default=None, alias='''uniqueItems''')
  contains: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None)
  max_properties: Optional[int] = Field(default=None, alias='''maxProperties''')
  min_properties: Optional[int] = Field(default=None, alias='''minProperties''')
  required: Optional[List[str]] = Field(default=None)
  additional_properties: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''additionalProperties''')
  definitions: Optional[dict[str, MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None)
  properties: Optional[dict[str, MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None)
  pattern_properties: Optional[dict[str, MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None, alias='''patternProperties''')
  dependencies: Optional[dict[str, Any | List[str]]] = Field(default=None)
  property_names: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''propertyNames''')
  const: Optional[Any] = Field(default=None)
  enum: Optional[List[Any]] = Field(default=None)
  type: Optional[JsonSchemaDraft07SchemaType.JsonSchemaDraft07SchemaType] = Field(default=None)
  format: Optional[str] = Field(default=None)
  content_media_type: Optional[str] = Field(default=None, alias='''contentMediaType''')
  content_encoding: Optional[str] = Field(default=None, alias='''contentEncoding''')
  reserved_if: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''if''')
  then: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None)
  reserved_else: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''else''')
  all_of: Optional[List[MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None, alias='''allOf''')
  any_of: Optional[List[MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None, alias='''anyOf''')
  one_of: Optional[List[MessageOneOf1OneOf1PayloadObject | bool]] = Field(default=None, alias='''oneOf''')
  reserved_not: Optional[Union[MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None, alias='''not''')
  discriminator: Optional[Union[SchemaAllOf1DiscriminatorObject.SchemaAllOf1DiscriminatorObject, str]] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(default=None, alias='''externalDocs''')
  deprecated: Optional[bool] = Field(default=None)
  nullable: Optional[bool] = Field(default=None)
  example: Optional[Any] = Field(default=None)
  xml: Optional[OpenapiSchema30Xml.OpenapiSchema30Xml] = Field(default=None)
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
    known_object_properties = ['dollar_id', 'dollar_schema', 'dollar_ref', 'dollar_comment', 'title', 'description', 'default', 'read_only', 'write_only', 'examples', 'multiple_of', 'maximum', 'exclusive_maximum', 'minimum', 'exclusive_minimum', 'max_length', 'min_length', 'pattern', 'additional_items', 'items', 'max_items', 'min_items', 'unique_items', 'contains', 'max_properties', 'min_properties', 'required', 'additional_properties', 'definitions', 'properties', 'pattern_properties', 'dependencies', 'property_names', 'const', 'enum', 'type', 'format', 'content_media_type', 'content_encoding', 'reserved_if', 'then', 'reserved_else', 'all_of', 'any_of', 'one_of', 'reserved_not', 'discriminator', 'external_docs', 'deprecated', 'nullable', 'example', 'xml', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['$id', '$schema', '$ref', '$comment', 'title', 'description', 'default', 'readOnly', 'writeOnly', 'examples', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'additionalItems', 'items', 'maxItems', 'minItems', 'uniqueItems', 'contains', 'maxProperties', 'minProperties', 'required', 'additionalProperties', 'definitions', 'properties', 'patternProperties', 'dependencies', 'propertyNames', 'const', 'enum', 'type', 'format', 'contentMediaType', 'contentEncoding', 'if', 'then', 'else', 'allOf', 'anyOf', 'oneOf', 'not', 'discriminator', 'externalDocs', 'deprecated', 'nullable', 'example', 'xml', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

