from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field

class MessageOneOf1OneOf1ExamplesItem(BaseModel): 
  headers: Optional[dict[str, Any]] = Field(default=None)
  payload: Optional[Any] = Field(default=None)
