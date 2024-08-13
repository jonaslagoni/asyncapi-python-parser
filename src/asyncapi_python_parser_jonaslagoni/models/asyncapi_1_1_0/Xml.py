from __future__ import annotations
from typing import Dict, Optional, Any, Union
from pydantic import BaseModel, Field

class Xml(BaseModel): 
  name: Optional[str] = Field(default=None)
  namespace: Optional[str] = Field(default=None)
  prefix: Optional[str] = Field(default=None)
  attribute: Optional[bool] = Field(default=None)
  wrapped: Optional[bool] = Field(default=None)
