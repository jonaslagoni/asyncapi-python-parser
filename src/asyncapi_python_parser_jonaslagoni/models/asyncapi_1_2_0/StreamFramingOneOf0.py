from __future__ import annotations
from typing import Dict, Optional, Any, Union
from pydantic import BaseModel, Field
from . import StreamFramingOneOf0Delimiter
class StreamFramingOneOf0(BaseModel): 
  type: Optional[str] = Field(default=None)
  delimiter: Optional[StreamFramingOneOf0Delimiter.StreamFramingOneOf0Delimiter] = Field(default=None)
