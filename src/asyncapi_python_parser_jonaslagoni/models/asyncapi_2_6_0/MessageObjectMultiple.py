from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import Reference
from . import MessageObject
class MessageObjectMultiple(BaseModel): 
  one_of: List[Reference.Reference | MessageObject.MessageObject] = Field(alias='''oneOf''')
