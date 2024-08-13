from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import SchemaObject
from . import Reference
from . import MessageOneOf1OneOf0
from . import MessageOneOf1OneOf1
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
from . import BindingsObject
class Components(BaseModel): 
  schemas: Optional[dict[str, SchemaObject.SchemaObject | bool]] = Field(default=None)
  messages: Optional[dict[str, Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]] = Field(default=None)
  security_schemes: Optional[dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect]] = Field(default=None, alias='''securitySchemes''')
  parameters: Optional[dict[str, Reference.Reference | Parameter.Parameter]] = Field(default=None)
  correlation_ids: Optional[dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]] = Field(default=None, alias='''correlationIds''')
  operation_traits: Optional[dict[str, OperationTrait.OperationTrait]] = Field(default=None, alias='''operationTraits''')
  message_traits: Optional[dict[str, MessageTrait.MessageTrait]] = Field(default=None, alias='''messageTraits''')
  server_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''serverBindings''')
  channel_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''channelBindings''')
  operation_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''operationBindings''')
  message_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''messageBindings''')
