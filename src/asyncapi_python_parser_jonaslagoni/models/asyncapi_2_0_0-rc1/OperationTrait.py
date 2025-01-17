from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Tag
from . import ExternalDocs
class OperationTrait(BaseModel): 
  summary: Optional[str] = Field(default=None)
  description: Optional[str] = Field(default=None)
  tags: Optional[List[Tag.Tag]] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''information about external documentation''', default=None, alias='''externalDocs''')
  operation_id: Optional[str] = Field(default=None, alias='''operationId''')
  protocol_info: Optional[dict[str, dict[str, Any]]] = Field(default=None, alias='''protocolInfo''')
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
    known_object_properties = ['summary', 'description', 'tags', 'external_docs', 'operation_id', 'protocol_info', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['summary', 'description', 'tags', 'externalDocs', 'operationId', 'protocolInfo', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

