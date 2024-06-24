from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import OperationTrait
from . import Tag
from . import ExternalDocs
from . import BindingsObject
from . import MessageOneOf1OneOf0
from . import MessageOneOf1OneOf1
class Operation(BaseModel): 
  traits: Optional[List[Reference.Reference | OperationTrait.OperationTrait]] = Field(default=None)
  summary: Optional[str] = Field(default=None)
  description: Optional[str] = Field(default=None)
  security: Optional[List[dict[str, List[str]]]] = Field(default=None)
  tags: Optional[List[Tag.Tag]] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(default=None, alias='''externalDocs''')
  operation_id: Optional[str] = Field(default=None, alias='''operationId''')
  bindings: Optional[BindingsObject.BindingsObject] = Field(default=None)
  message: Optional[Union[Reference.Reference, MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]] = Field(default=None)
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
    known_object_properties = ['traits', 'summary', 'description', 'security', 'tags', 'external_docs', 'operation_id', 'bindings', 'message', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['traits', 'summary', 'description', 'security', 'tags', 'externalDocs', 'operationId', 'bindings', 'message', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

