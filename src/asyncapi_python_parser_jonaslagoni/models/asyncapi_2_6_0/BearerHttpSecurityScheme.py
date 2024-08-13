from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field

class BearerHttpSecurityScheme(BaseModel): 
  scheme: str = Field(description='''The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235.''')
  bearer_format: Optional[str] = Field(description='''A hint to the client to identify how the bearer token is formatted.''', default=None, alias='''bearerFormat''')
  type: str = Field(description='''The type of the security scheme. ''')
  description: Optional[str] = Field(description='''A short description for security scheme.''', default=None)
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
    known_object_properties = ['scheme', 'bearer_format', 'type', 'description', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['scheme', 'bearerFormat', 'type', 'description', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

