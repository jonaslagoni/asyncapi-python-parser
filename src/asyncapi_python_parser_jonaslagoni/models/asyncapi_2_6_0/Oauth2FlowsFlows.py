from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field
from . import Oauth2FlowsFlowsImplicit
from . import Oauth2FlowsFlowsPassword
from . import Oauth2FlowsFlowsClientCredentials
from . import Oauth2FlowsFlowsAuthorizationCode
class Oauth2FlowsFlows(BaseModel): 
  implicit: Optional[Oauth2FlowsFlowsImplicit.Oauth2FlowsFlowsImplicit] = Field(description='''Configuration for the OAuth Implicit flow.''', default=None)
  password: Optional[Oauth2FlowsFlowsPassword.Oauth2FlowsFlowsPassword] = Field(description='''Configuration for the OAuth Resource Owner Protected Credentials flow.''', default=None)
  client_credentials: Optional[Oauth2FlowsFlowsClientCredentials.Oauth2FlowsFlowsClientCredentials] = Field(description='''Configuration for the OAuth Client Credentials flow.''', default=None, alias='''clientCredentials''')
  authorization_code: Optional[Oauth2FlowsFlowsAuthorizationCode.Oauth2FlowsFlowsAuthorizationCode] = Field(description='''Configuration for the OAuth Authorization Code flow.''', default=None, alias='''authorizationCode''')
