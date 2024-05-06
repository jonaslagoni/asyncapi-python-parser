from enum import Enum

class ApiKeyHttpSecuritySchemeIn(Enum): 
  HEADER = "header"
  QUERY = "query"
  COOKIE = "cookie"