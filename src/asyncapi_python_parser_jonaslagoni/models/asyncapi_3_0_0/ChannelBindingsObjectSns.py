from __future__ import annotations
import json
from typing import Any, Dict
from . import ChannelSchema
class ChannelBindingsObjectSns: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: str = input['binding_version']
    if 'name' in input:
      self._name: str = input['name']
    if 'ordering' in input:
      self._ordering: ChannelSchema.ChannelSchema = ChannelSchema.ChannelSchema(input['ordering'])
    if 'policy' in input:
      self._policy: ChannelSchema.ChannelSchema = ChannelSchema.ChannelSchema(input['policy'])
    if 'tags' in input:
      self._tags: dict[str, Any] = input['tags']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> str:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: str):
    self._binding_version = binding_version

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def ordering(self) -> ChannelSchema.ChannelSchema:
    return self._ordering
  @ordering.setter
  def ordering(self, ordering: ChannelSchema.ChannelSchema):
    self._ordering = ordering

  @property
  def policy(self) -> ChannelSchema.ChannelSchema:
    return self._policy
  @policy.setter
  def policy(self, policy: ChannelSchema.ChannelSchema):
    self._policy = policy

  @property
  def tags(self) -> dict[str, Any]:
    return self._tags
  @tags.setter
  def tags(self, tags: dict[str, Any]):
    self._tags = tags

  @property
  def extensions(self) -> dict[str, Any]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return ChannelBindingsObjectSns(**json.loads(json_string))
