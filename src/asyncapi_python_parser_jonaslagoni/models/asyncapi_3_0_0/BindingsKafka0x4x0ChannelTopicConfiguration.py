from __future__ import annotations
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field
from . import BindingsKafka0x4x0ChannelTopicConfigurationCleanupxpolicyItem
class BindingsKafka0x4x0ChannelTopicConfiguration(BaseModel): 
  cleanup_dot_policy: Optional[List[BindingsKafka0x4x0ChannelTopicConfigurationCleanupxpolicyItem.BindingsKafka0x4x0ChannelTopicConfigurationCleanupxpolicyItem]] = Field(default=None, alias='''cleanup.policy''')
  retention_dot_ms: Optional[int] = Field(default=None, alias='''retention.ms''')
  retention_dot_bytes: Optional[int] = Field(default=None, alias='''retention.bytes''')
  delete_dot_retention_dot_ms: Optional[int] = Field(default=None, alias='''delete.retention.ms''')
  max_dot_message_dot_bytes: Optional[int] = Field(default=None, alias='''max.message.bytes''')
