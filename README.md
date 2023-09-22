# jsonapi
The customized APIs extended from json library are designed to achieve (de)serialization of complex and range inputs.

# Installation
`pip install -e .` to install the package
`python` to open Python
`import jsonapi as js` to import jsonapi
`js.dumps(1+2j)` to encode complex(1.0, 2.0) to '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'
`js.loads('{"start": 1, "stop": 10, "step": 1, "__extended_json_type__": "range"}')` to decode the json output to range(1, 10)

# Packaging and Distribution
`python -m build`  
This package is able to be built and wheel distributed locally. A new `dist/` folder can be successfully generated.
