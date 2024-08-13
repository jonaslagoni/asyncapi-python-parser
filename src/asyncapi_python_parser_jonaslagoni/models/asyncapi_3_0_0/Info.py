from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Contact
from . import License
from . import Reference
from . import Tag
from . import ExternalDocs
class Info(BaseModel): 
  title: str = Field(description='''A unique and precise title of the API.''')
  version: str = Field(description='''A semantic version number of the API.''')
  description: Optional[str] = Field(description='''A longer description of the API. Should be different from the title. CommonMark is allowed.''', default=None)
  terms_of_service: Optional[str] = Field(description='''A URL to the Terms of Service for the API. MUST be in the format of a URL.''', default=None, alias='''termsOfService''')
  contact: Optional[Contact.Contact] = Field(description='''Contact information for the exposed API.''', default=None)
  license: Optional[License.License] = Field(default=None)
  tags: Optional[List[Reference.Reference | Tag.Tag]] = Field(description='''A list of tags for application API documentation control. Tags can be used for logical grouping of applications.''', default=None)
  external_docs: Optional[Union[Reference.Reference, ExternalDocs.ExternalDocs]] = Field(default=None, alias='''externalDocs''')
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
    known_object_properties = ['title', 'version', 'description', 'terms_of_service', 'contact', 'license', 'tags', 'external_docs', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['title', 'version', 'description', 'termsOfService', 'contact', 'license', 'tags', 'externalDocs', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

