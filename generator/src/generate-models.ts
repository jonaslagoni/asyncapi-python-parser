import { PYTHON_JSON_SERIALIZER_PRESET, PythonFileGenerator } from '@asyncapi/modelina';
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
  const outputDirForVersion = path.resolve(__dirname, outputDir, `asyncapi_${input.asyncapiVersion}`);
  // if (fs.existsSync(outputDirForVersion)) {
  //   fs.rmSync(outputDirForVersion, { recursive: true });
  // }
  const generator = new PythonFileGenerator({ 
    importsStyle: 'implicit',
    presets: [
      PYTHON_JSON_SERIALIZER_PRESET],
  });
  
  await generator.generateToFiles(inputObj, outputDirForVersion, {});
}

async function generate() {
  for (const file of filteredFiles) {
    await defaultGenerateModels(file, outputDirectoryPath);
  }
}
generate();
