import { FormatHelpers, PYTHON_PYDANTIC_PRESET, PythonDefaultModelNameConstraints, PythonFileGenerator, pythonDefaultEnumKeyConstraints, pythonDefaultModelNameConstraints } from '@asyncapi/modelina';
import * as path from 'path';
import * as fs from 'fs';

const outputDirectoryPath = path.resolve(__dirname, '../../src/asyncapi_python_parser_jonaslagoni/models');
const schemaFiles = path.resolve(__dirname, '../definitions');
interface FileReadType {
  fileContent: string
  fileName: string
  filePath: string
  asyncapiVersion: string
}
const filteredFiles: FileReadType[] = fs.readdirSync(schemaFiles).map((file) => {
  const absPath = path.resolve(schemaFiles, file);
  return {
    fileContent: fs.readFileSync(absPath).toString(),
    fileName: path.basename(file),
    filePath: absPath,
    asyncapiVersion: path.basename(file).replace('-without-$id.json', '').replace(/\./g, '_')
  }
});

async function defaultGenerateModels(input: FileReadType, outputDir: string) {
  const inputObj = JSON.parse(String(input.fileContent));
  if(input.asyncapiVersion === '3_0_0') {
    inputObj['definitions']['avroSchema_v1'] = {}
    inputObj['definitions']['schema'] = {"$ref": "#/definitions/json-schema-draft-07-schema"}
    inputObj['definitions']['anySchema'] = {"oneOf": [{"$ref": "#/definitions/multiFormatSchema"}, {"$ref": "#/definitions/json-schema-draft-07-schema"}]}
  } else if(["2.6.0", "2.5.0", "2.4.0", "2.3.0", "2.2.0", "2.1.0", "2.0.0"].includes(input.asyncapiVersion)) {
    inputObj['definitions']['MultipleMessages'] = {
      "type": "object",
      "required": [
          "oneOf"
      ],
      "additionalProperties": false,
      "properties": {
          "oneOf": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                      "$ref": "#/definitions/Reference"
                  },
                  {
                      "$ref": "#/definitions/MessageObject"
                  }
                ]
              }
          }
      }
    }
    inputObj['definitions']['MessageObject'] = {
      "type": "object",
      "additionalProperties": false,
      "patternProperties": {
          "^x-[\\w\\d\\.\\x2d_]+$": {
              "$ref": "#/definitions/specificationExtension"
          }
      },
      "properties": {
          "schemaFormat": {
              "type": "string"
          },
          "contentType": {
              "type": "string"
          },
          "headers": {
              "allOf": [
                  {
                      "$ref": "#/definitions/schema"
                  },
                  {
                      "properties": {
                          "type": {
                              "const": "object"
                          }
                      }
                  }
              ]
          },
          "messageId": {
              "type": "string"
          },
          "payload": {},
          "correlationId": {
              "oneOf": [
                  {
                      "$ref": "#/definitions/Reference"
                  },
                  {
                      "$ref": "#/definitions/correlationId"
                  }
              ]
          },
          "tags": {
              "type": "array",
              "items": {
                  "$ref": "#/definitions/tag"
              },
              "uniqueItems": true
          },
          "summary": {
              "type": "string",
              "description": "A brief summary of the message."
          },
          "name": {
              "type": "string",
              "description": "Name of the message."
          },
          "title": {
              "type": "string",
              "description": "A human-friendly title for the message."
          },
          "description": {
              "type": "string",
              "description": "A longer description of the message. CommonMark is allowed."
          },
          "externalDocs": {
              "$ref": "#/definitions/externalDocs"
          },
          "deprecated": {
              "type": "boolean",
              "default": false
          },
          "examples": {
              "type": "array",
              "description": "List of examples.",
              "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "anyOf": [
                      {
                          "required": [
                              "payload"
                          ]
                      },
                      {
                          "required": [
                              "headers"
                          ]
                      }
                  ],
                  "properties": {
                      "name": {
                          "type": "string",
                          "description": "Machine readable name of the message example."
                      },
                      "summary": {
                          "type": "string",
                          "description": "A brief summary of the message example."
                      },
                      "headers": {
                          "type": "object",
                          "description": "Schema definition of the application headers."
                      },
                      "payload": {
                          "description": "Definition of the message payload. It can be of any type"
                      }
                  }
              }
          },
          "bindings": {
              "$ref": "#/definitions/bindingsObject"
          },
          "traits": {
              "type": "array",
              "items": {
                  "oneOf": [
                      {
                          "$ref": "#/definitions/Reference"
                      },
                      {
                          "$ref": "#/definitions/messageTrait"
                      }
                  ]
              }
          }
      },
      "allOf": [
          {
              "if": {
                  "not": {
                      "required": [
                          "schemaFormat"
                      ]
                  }
              },
              "then": {
                  "properties": {
                      "payload": {
                          "$ref": "#/definitions/schema"
                      }
                  }
              }
          },
          {
              "if": {
                  "required": [
                      "schemaFormat"
                  ],
                  "properties": {
                      "schemaFormat": {
                          "enum": [
                              "application/vnd.aai.asyncapi;version=2.0.0",
                              "application/vnd.aai.asyncapi+json;version=2.0.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.0.0",
                              "application/vnd.aai.asyncapi;version=2.1.0",
                              "application/vnd.aai.asyncapi+json;version=2.1.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.1.0",
                              "application/vnd.aai.asyncapi;version=2.2.0",
                              "application/vnd.aai.asyncapi+json;version=2.2.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.2.0",
                              "application/vnd.aai.asyncapi;version=2.3.0",
                              "application/vnd.aai.asyncapi+json;version=2.3.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.3.0",
                              "application/vnd.aai.asyncapi;version=2.4.0",
                              "application/vnd.aai.asyncapi+json;version=2.4.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.4.0",
                              "application/vnd.aai.asyncapi;version=2.5.0",
                              "application/vnd.aai.asyncapi+json;version=2.5.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.5.0",
                              "application/vnd.aai.asyncapi;version=2.6.0",
                              "application/vnd.aai.asyncapi+json;version=2.6.0",
                              "application/vnd.aai.asyncapi+yaml;version=2.6.0"
                          ]
                      }
                  }
              },
              "then": {
                  "properties": {
                      "payload": {
                          "$ref": "#/definitions/schema"
                      }
                  }
              }
          },
          {
              "if": {
                  "required": [
                      "schemaFormat"
                  ],
                  "properties": {
                      "schemaFormat": {
                          "enum": [
                              "application/schema+json;version=draft-07",
                              "application/schema+yaml;version=draft-07"
                          ]
                      }
                  }
              },
              "then": {
                  "properties": {
                      "payload": {
                          "$ref": "#/definitions/json-schema-draft-07-schema"
                      }
                  }
              }
          },
          {
              "if": {
                  "required": [
                      "schemaFormat"
                  ],
                  "properties": {
                      "schemaFormat": {
                          "enum": [
                              "application/vnd.oai.openapi;version=3.0.0",
                              "application/vnd.oai.openapi+json;version=3.0.0",
                              "application/vnd.oai.openapi+yaml;version=3.0.0"
                          ]
                      }
                  }
              },
              "then": {
                  "properties": {
                      "payload": {
                          "$ref": "#/definitions/openapiSchema_3_0"
                      }
                  }
              }
          },
          {
              "if": {
                  "required": [
                      "schemaFormat"
                  ],
                  "properties": {
                      "schemaFormat": {
                          "enum": [
                              "application/vnd.apache.avro;version=1.9.0",
                              "application/vnd.apache.avro+json;version=1.9.0",
                              "application/vnd.apache.avro+yaml;version=1.9.0"
                          ]
                      }
                  }
              },
              "then": {
                  "properties": {
                      "payload": {
                          "$ref": "#/definitions/avroSchema_v1"
                      }
                  }
              }
          }
      ]
    }
    inputObj['definitions']['message'] = {
      "description": "Describes a message received on a given channel and operation.",
      "oneOf": [
          {
              "$ref": "#/definitions/Reference"
          },
          {
              "$ref": "#/definitions/MultipleMessages"
          },
          {
              "$ref": "#/definitions/MessageObject"
          }
      ]
    }
  }
  const outputDirForVersion = path.resolve(__dirname, outputDir, `asyncapi_${input.asyncapiVersion}`);
  if (fs.existsSync(outputDirForVersion)) {
    fs.rmSync(outputDirForVersion, { recursive: true });
  }
  const generator = new PythonFileGenerator({ 
    importsStyle: 'implicit',
    constraints: {
      modelName: pythonDefaultModelNameConstraints({
        NO_SPECIAL_CHAR: (value: string) => {
          value = value.replace(/\./gi, 'x')
          if(value.includes('binding')) {
            return FormatHelpers.replaceSpecialCharacters(value, {
              exclude: [' ', '_', '-'],
              separator: '_'
            });
          } else {
            return value.replace(/[^\w\s]/gi, ' ')
          }
        },
        NO_RESERVED_KEYWORDS: (value: string) => {
          const customReserved = ['record', 'field'];
          value = PythonDefaultModelNameConstraints.NO_RESERVED_KEYWORDS(value);
          const isReserved = customReserved.includes(value.toLowerCase());
          if(isReserved) {
            value = `reserved_${value}`
          }
          return value;
        }
      }),
      enumKey: pythonDefaultEnumKeyConstraints({
        NO_NUMBER_START_CHAR(value) {
          const firstChar = value.charAt(0);
          if (firstChar !== '' && !isNaN(+firstChar)) {
            return `v_${value}`;
          }
          return value;
        },
        NO_SPECIAL_CHAR(value) {
          return value.replace(/[^\w\s]/gi, ' ')
        }
      })
    },
    processorOptions: {
      jsonSchema: {
        propertyNameForAdditionalProperties: 'extensions',
        interpretSingleEnumAsConst: true
      }
    },
    presets: [
      PYTHON_PYDANTIC_PRESET
    ],
  });
  
  await generator.generateToFiles(inputObj, outputDirForVersion, {});
}

async function generate() {
  for (const file of filteredFiles) {
    await defaultGenerateModels(file, outputDirectoryPath);
  }
}
generate();
