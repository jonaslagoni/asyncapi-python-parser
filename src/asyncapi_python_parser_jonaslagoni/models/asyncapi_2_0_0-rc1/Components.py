from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import Schema
from . import Message
from . import Reference
from . import UserPassword
from . import ApiKey
from . import X509
from . import SymmetricEncryption
from . import AsymmetricEncryption
from . import BearerHttpSecurityScheme
from . import ApiKeyHttpSecurityScheme
from . import Oauth2Flows
from . import OpenIdConnect
from . import Parameter
from . import CorrelationId
from . import OperationTrait
from . import MessageTrait
class Components(BaseModel): 
  schemas: Optional[dict[str, Schema.Schema]] = Field(default=None)
  messages: Optional[dict[str, Message.Message]] = Field(default=None)
  security_schemes: Optional[dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect]] = Field(default=None, alias='''securitySchemes''')
  parameters: Optional[dict[str, Reference.Reference | Parameter.Parameter]] = Field(default=None)
  correlation_ids: Optional[dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]] = Field(default=None, alias='''correlationIds''')
  traits: Optional[dict[str, OperationTrait.OperationTrait | MessageTrait.MessageTrait]] = Field(default=None)
