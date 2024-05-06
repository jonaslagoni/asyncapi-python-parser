import unittest
from src.asyncapi_python_parser_jonaslagoni.traits import apply_traits

class TestTraits(unittest.TestCase):
  def test_traits_are_applied_correctly_for_v3(self):
    """
    Test that we can apply traits for v3 in all locations
    """
    message = {
        "traits": [
            {
                "summary": "test"
            }
        ],
        "payload": {
            "type": "object",
            "properties": {
                "displayName": {
                    "type": "string",
                    "description": "Name of the user"
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "Email of the user"
                }
            }
        }
    }
    operation = {
        "traits": [
            {
                "summary": "test"
            }
        ],
        "action": "send",
        "channel": {
            "address": "user/signedup",
            "messages": {
                "UserSignedUp": message
            }
        },
        "messages": {
            "UserSignedUp": message
        }
    }
    channel = {
        "address": "user/signedup",
        "messages": {
            "UserSignedUp": message
        }
    }
    data = {
        "asyncapi": "3.0.0",
        "channels": {
            "userSignedup": channel
        },
        "operations": {
            "sendUserSignedup": operation
        },
        "components": {
            "operations": {
                "sendUserSignedup": operation
            },
            "messages": {
                "UserSignedUp": message
            },
            "channels": {
                "userSignedup": channel
            }
        }
    }
    apply_traits(data)
    print(data)
    self.assertEqual('test', data["channels"]["userSignedup"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["operations"]["sendUserSignedup"]["summary"])
    self.assertEqual('test', data["operations"]["sendUserSignedup"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["operations"]["sendUserSignedup"]["channel"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["components"]["operations"]["sendUserSignedup"]["summary"])
    self.assertEqual('test', data["components"]["operations"]["sendUserSignedup"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["components"]["operations"]["sendUserSignedup"]["channel"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["components"]["channels"]["userSignedup"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('test', data["components"]["messages"]["UserSignedUp"]["summary"])
    
  def test_traits_are_applied_correctly_for_v2(self):
    """
    Test that we can apply traits for v2 in all locations
    """
    message = {
        "traits": [
            {
                "summary": "test",
                "description": "new"
            }
        ],
        "description": "old",
        "payload": {
            "type": "object",
            "properties": {
                "displayName": {
                    "type": "string",
                    "description": "Name of the user"
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "Email of the user"
                }
            }
        }
    }
    operation = {
        "traits": [
            {
                "summary": "test",
                "description": "new"
            }
        ],
        "description": "old",
        "message": message
    }
    operation_one_of = {
        "traits": [
            {
                "summary": "test",
                "description": "new"
            }
        ],
        "description": "old",
        "message": {
            "oneOf": [
                message
            ]
        }
    }
    channel = {
        "publish": operation,
        "subscribe": operation_one_of
    }
    data = {
        "asyncapi": "2.6.0",
        "channels": {
            "user/signedup": channel
        },
        "components": {
            "messages": {
                "UserSignedUp": message
            },
            "channels": {
                "user/signedup": channel
            }
        }
    }
    apply_traits(data)

    self.assertEqual('test', data["channels"]["user/signedup"]["publish"]["summary"])
    self.assertEqual('old', data["channels"]["user/signedup"]["publish"]["description"])
    self.assertEqual('test', data["channels"]["user/signedup"]["publish"]["message"]["summary"])
    self.assertEqual('old', data["channels"]["user/signedup"]["publish"]["message"]["description"])
    self.assertEqual('test', data["channels"]["user/signedup"]["subscribe"]["summary"])
    self.assertEqual('old', data["channels"]["user/signedup"]["subscribe"]["description"])
    self.assertEqual('test', data["channels"]["user/signedup"]["subscribe"]["message"]["oneOf"][0]["summary"])
    self.assertEqual('old', data["channels"]["user/signedup"]["subscribe"]["message"]["oneOf"][0]["description"])
    
    
    self.assertEqual('test', data["components"]["channels"]["user/signedup"]["publish"]["summary"])
    self.assertEqual('old', data["components"]["channels"]["user/signedup"]["publish"]["description"])
    self.assertEqual('test', data["components"]["channels"]["user/signedup"]["publish"]["message"]["summary"])
    self.assertEqual('old', data["components"]["channels"]["user/signedup"]["publish"]["message"]["description"])
    self.assertEqual('test', data["components"]["channels"]["user/signedup"]["subscribe"]["summary"])
    self.assertEqual('old', data["components"]["channels"]["user/signedup"]["subscribe"]["description"])
    self.assertEqual('test', data["components"]["channels"]["user/signedup"]["subscribe"]["message"]["oneOf"][0]["summary"])
    self.assertEqual('old', data["components"]["channels"]["user/signedup"]["subscribe"]["message"]["oneOf"][0]["description"])
    
    self.assertEqual('test', data["components"]["messages"]["UserSignedUp"]["summary"])
    self.assertEqual('old', data["components"]["messages"]["UserSignedUp"]["description"])
if __name__ == '__main__':
    unittest.main()