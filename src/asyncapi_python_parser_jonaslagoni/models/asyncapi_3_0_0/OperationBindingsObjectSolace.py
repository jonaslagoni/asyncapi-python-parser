from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import OperationBindingsObjectSolaceBindingVersion
from . import BindingsSolace0x3x0OperationDestinationsItemOneOf0
from . import BindingsSolace0x3x0OperationDestinationsItemOneOf1
class OperationBindingsObjectSolace(BaseModel): 
  binding_version: Optional[OperationBindingsObjectSolaceBindingVersion.OperationBindingsObjectSolaceBindingVersion] = Field(default=None, alias='''bindingVersion''')
  destinations: Optional[List[BindingsSolace0x3x0OperationDestinationsItemOneOf0.BindingsSolace0x3x0OperationDestinationsItemOneOf0 | BindingsSolace0x3x0OperationDestinationsItemOneOf1.BindingsSolace0x3x0OperationDestinationsItemOneOf1]] = Field(default=None)
