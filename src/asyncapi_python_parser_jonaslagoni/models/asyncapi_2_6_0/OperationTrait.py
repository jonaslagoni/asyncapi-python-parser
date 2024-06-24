from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Tag
from . import ExternalDocs
from . import BindingsObject
class OperationTrait(BaseModel): 
  summary: Optional[str] = Field(description='''A short summary of what the operation is about.''', default=None)
  description: Optional[str] = Field(description='''A verbose explanation of the operation.''', default=None)
  tags: Optional[List[Tag.Tag]] = Field(description='''A list of tags for logical grouping and categorization of operations.''', default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''Allows referencing an external resource for extended documentation.''', default=None, alias='''externalDocs''')
  operation_id: Optional[str] = Field(description='''Unique string used to identify the operation. The id MUST be unique among all operations described in the API.''', default=None, alias='''operationId''')
  security: Optional[List[dict[str, List[str]]]] = Field(description='''A declaration of which security mechanisms are associated with this operation. ''', default=None)
  bindings: Optional[BindingsObject.BindingsObject] = Field(description='''Map describing protocol-specific definitions for a server.''', default=None)
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
    known_object_properties = ['summary', 'description', 'tags', 'external_docs', 'operation_id', 'security', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['summary', 'description', 'tags', 'externalDocs', 'operationId', 'security', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

