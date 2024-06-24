from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field

class Oauth2FlowsFlowsClientCredentials(BaseModel): 
  authorization_url: Optional[str] = Field(description='''The authorization URL to be used for this flow. This MUST be in the form of an absolute URL.''', default=None, alias='''authorizationUrl''')
  token_url: str = Field(description='''The token URL to be used for this flow. This MUST be in the form of an absolute URL.''', alias='''tokenUrl''')
  refresh_url: Optional[str] = Field(description='''The URL to be used for obtaining refresh tokens. This MUST be in the form of an absolute URL.''', default=None, alias='''refreshUrl''')
  available_scopes: dict[str, str] = Field(alias='''availableScopes''')
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
    known_object_properties = ['authorization_url', 'token_url', 'refresh_url', 'available_scopes', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['authorizationUrl', 'tokenUrl', 'refreshUrl', 'availableScopes', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

