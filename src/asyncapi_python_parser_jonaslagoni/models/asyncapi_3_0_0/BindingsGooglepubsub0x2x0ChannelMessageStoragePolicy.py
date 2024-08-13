from __future__ import annotations
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field

class BindingsGooglepubsub0x2x0ChannelMessageStoragePolicy(BaseModel): 
  allowed_persistence_regions: Optional[List[str]] = Field(default=None, alias='''allowedPersistenceRegions''')
