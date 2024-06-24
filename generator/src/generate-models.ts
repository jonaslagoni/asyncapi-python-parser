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
  inputObj['definitions']['avroSchema_v1'] = {}
  inputObj['definitions']['schema'] = {"$ref": "#/definitions/json-schema-draft-07-schema"}
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
          value = value.replace(/\./gi, '_')
          return FormatHelpers.replaceSpecialCharacters(value, {
            exclude: [' ', '_'],
            separator: '_'
          });
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
