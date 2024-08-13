from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import OperationTrait
from . import Tag
from . import ExternalDocs
from . import BindingsObject
from . import MessageObjectMultiple
from . import MessageObject
class Operation(BaseModel): 
  traits: Optional[List[Reference.Reference | OperationTrait.OperationTrait]] = Field(description='''A list of traits to apply to the operation object.''', default=None)
  summary: Optional[str] = Field(description='''A short summary of what the operation is about.''', default=None)
  description: Optional[str] = Field(description='''A verbose explanation of the operation.''', default=None)
  security: Optional[List[dict[str, List[str]]]] = Field(description='''A declaration of which security mechanisms are associated with this operation.''', default=None)
  tags: Optional[List[Tag.Tag]] = Field(description='''A list of tags for logical grouping and categorization of operations.''', default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''Allows referencing an external resource for extended documentation.''', default=None, alias='''externalDocs''')
  operation_id: Optional[str] = Field(default=None, alias='''operationId''')
  bindings: Optional[BindingsObject.BindingsObject] = Field(description='''Map describing protocol-specific definitions for a server.''', default=None)
  message: Optional[Union[Reference.Reference, MessageObjectMultiple.MessageObjectMultiple, MessageObject.MessageObject]] = Field(description='''Describes a message received on a given channel and operation.''', default=None)
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

