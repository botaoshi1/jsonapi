# jsonapi
The customized APIs extended from json library are designed to achieve (de)serialization of complex and range inputs.

# Install
pip install jsonapi/pip3 install jsonapi

# Serialization
json.dumps(obj, cls=ExtendedEncoder)

# Deserialization
json.loads(s, cls=ExtendedDecoder)

Tests are all passed with various test cases.
