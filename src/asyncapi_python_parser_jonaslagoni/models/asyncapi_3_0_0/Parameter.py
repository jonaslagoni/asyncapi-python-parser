from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field

class Parameter(BaseModel): 
  description: Optional[str] = Field(description='''A brief description of the parameter. This could contain examples of use. GitHub Flavored Markdown is allowed.''', default=None)
  enum: Optional[List[str]] = Field(description='''An enumeration of string values to be used if the substitution options are from a limited set.''', default=None)
  default: Optional[str] = Field(description='''The default value to use for substitution, and to send, if an alternate value is not supplied.''', default=None)
  examples: Optional[List[str]] = Field(description='''An array of examples of the parameter value.''', default=None)
  location: Optional[str] = Field(description='''A runtime expression that specifies the location of the parameter value''', default=None)
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
    known_object_properties = ['description', 'enum', 'default', 'examples', 'location', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['description', 'enum', 'default', 'examples', 'location', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

