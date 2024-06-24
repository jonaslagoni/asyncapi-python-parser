from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import Reference
from . import MessageOneOf1OneOf1
class MessageOneOf1OneOf0(BaseModel): 
  one_of: List[Reference.Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1] = Field(alias='''oneOf''')
