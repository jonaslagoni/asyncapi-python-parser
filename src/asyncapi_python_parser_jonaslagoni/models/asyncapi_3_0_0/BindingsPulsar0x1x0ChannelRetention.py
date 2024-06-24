from __future__ import annotations
from typing import Dict, Optional, Any, Union
from pydantic import BaseModel, Field

class BindingsPulsar0x1x0ChannelRetention(BaseModel): 
  time: Optional[int] = Field(default=None)
  size: Optional[int] = Field(default=None)
