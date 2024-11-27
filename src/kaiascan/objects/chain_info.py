"""
This module defines configuration constants for interacting with blockchain networks.

The `CHAIN_INFO` dictionary provides essential details for connecting to both 
mainnet and testnet environments of a blockchain system. It includes base URLs for 
API endpoints and corresponding chain IDs, facilitating seamless network switching 
in applications that interact with the blockchain.

Usage:
    These constants can be used in blockchain explorers, wallets, or other 
    decentralized applications requiring network-specific configurations.
"""

CHAIN_INFO = {
    "BASE_URL_MAINNET": "https://mainnet-oapi.kaiascan.io/",
    "BASE_URL_TESTNET": "https://kairos-oapi.kaiascan.io/",
    "CHAIN_ID_MAINNET": "8217",
    "CHAIN_ID_TESTNET": "1001",
}
