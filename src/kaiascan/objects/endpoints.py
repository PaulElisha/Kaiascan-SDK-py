"""
This module defines API endpoint paths for interacting with various blockchain resources.

The `ENDPOINTS` dictionary provides a centralized mapping of endpoint paths used 
to access different blockchain-related data, such as tokens, NFTs, blocks, 
transactions, contracts, and transaction receipts. These paths can be appended 
to a base URL to form complete API requests.

Usage:
    These endpoint paths can be used in applications that interact with blockchain APIs, 
    making it easy to construct and manage API calls to retrieve blockchain data.
"""

ENDPOINTS = {
    "tokens_endpoint": "api/v1/tokens",
    "nfts_endpoint": "api/v1/nfts",
    "blocks_endpoint": "api/v1/blocks",
    "transaction_endpoint": "api/v1/transactions",
    "contract_endpoint": "api/v1/contracts",
    "transaction_receipts_endpoint": "api/v1/transaction-receipts",
}
