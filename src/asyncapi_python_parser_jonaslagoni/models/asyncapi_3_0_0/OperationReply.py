from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import OperationReplyAddress
class OperationReply(BaseModel): 
  address: Optional[Union[Reference.Reference, OperationReplyAddress.OperationReplyAddress]] = Field(default=None)
  channel: Optional[Reference.Reference] = Field(description='''A simple object to allow referencing other components in the specification, internally and externally.''', default=None)
  messages: Optional[List[Reference.Reference]] = Field(description='''A list of $ref pointers pointing to the supported Message Objects that can be processed by this operation as reply. It MUST contain a subset of the messages defined in the channel referenced in this operation reply. Every message processed by this operation MUST be valid against one, and only one, of the message objects referenced in this list. Please note the messages property value MUST be a list of Reference Objects and, therefore, MUST NOT contain Message Objects. However, it is RECOMMENDED that parsers (or other software) dereference this property for a better development experience.''', default=None)
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
    known_object_properties = ['address', 'channel', 'messages', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['address', 'channel', 'messages', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

