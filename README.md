# JSONAPI

A Python package for custom JSON encoding and decoding.

## Installation

```bash
pip install jsonapi
```

## Usage

### Custom JSON Encoding and Decoding

```python
import json
from jsonapi.jsonapi import dumps, loads

data = {
    "complexValue": complex(1, 2),
    "rangeValue": list(range(5, 300, 3)), 73: False,
}

# JSON serialization with custom encoder
json_data = dumps(data)

# JSON deserialization with custom decoder
decoded_data = loads(json_data)

print("Serialized data is ", json_data)
print("Deserialized data is ", decoded_data)

```