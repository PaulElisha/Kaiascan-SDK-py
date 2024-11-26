# Kaiascan Python SDK

A Python SDK for interacting with the Kaiascan API.

## Installation

```bash
pip install kaiascan
```

## Usage

```python
from kaiascan import KaiascanSDK

# Initialize the SDK

sdk = KaiascanSDK(is_testnet=True)

# Get token information
token_info = sdk.get_fungible_token("0x...")
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements_dev.txt`
3. Run tests: `pytest`
