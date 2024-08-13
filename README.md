# Python AsyncAPI Parser

## Parsing options
These are the options that can be provided when parsing AsyncAPI documents;

### Reference resolvement
By default, all references are resolved when the document is parsed, however, if wanted you can turn this off by providing the option `resolve_references` when parsing a document.

```py
parse(data, ParserOptions({'resolve_references': True}))
```

### Validating input

By default, the input is validated against the [official AsyncAPI JSON Schema documents](https://github.com/asyncapi/spec-json-schemas/), however, if wanted you can turn this off by providing the option `validate_input` when parsing a document.

```py
parse(data, ParserOptions({'validate_input': True}))
```

### Applying traits

By default, traits are applied when parsed, however, if wanted you can turn this off by providing the option `apply_traits`. 

```py
parse(data, ParserOptions({'apply_traits': True}))
```

## Serializing parsed documents

All parts of the parsed AsyncAPI document can be serialized back into JSON.

```py
document = {}
parsedDocument = parse(data)
serializedDocument = parsedDocument.json()
```

> NOTICE: If `traits` or `references` have been applied, `document` and `serializedDocument` will never be the same.

## Creating new AsyncAPI documents

Through the AsyncAPI Python models, you can create AsyncAPI documents directly in your code instead of parsing existing documents.

```py
document = AsyncApi2Dot0Dot0SchemaDot({'asyncapi': '3.0.0', 'info': {'title': 'smartylighting', 'version': '1.0.0'}})
```

## Reading and Overwriting values
You can also overwrite existing functions 
```py
document = AsyncApi2Dot0Dot0SchemaDot({'asyncapi': '3.0.0', 'info': {'title': 'smartylighting', 'version': '1.0.0'}})
document.id('urn:example:com:smartylighting:streetlights:server')
```

# Restrictions

These are the current known restrictions;
- Private reference