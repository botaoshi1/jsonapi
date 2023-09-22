# jsonapi
The customized APIs extended from json library are designed to achieve (de)serialization of complex and range inputs.

# Serialization
`json.dumps(obj, cls=ExtendedEncoder)`
This function is able to encode complex/range objects to json-readable data.

# Deserialization
`json.loads(s, cls=ExtendedDecoder)`
This function is able to decode json-readable data to complex/range objects.

# Packaging and Distribution
`python -m build`
This package is able to be built and wheel distributed locally. A new `dist/` folder can be successfully generated.
