from __future__ import annotations
from typing import Dict, Optional, Any, Union
from pydantic import BaseModel, Field

class StreamFramingOneOf1(BaseModel): 
  type: Optional[str] = Field(default=None)
  delimiter: Optional[str] = Field(default=None)
