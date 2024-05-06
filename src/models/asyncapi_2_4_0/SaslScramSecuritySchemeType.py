from enum import Enum

class SaslScramSecuritySchemeType(Enum): 
  SCRAM_SHA256 = "scramSha256"
  SCRAM_SHA512 = "scramSha512"