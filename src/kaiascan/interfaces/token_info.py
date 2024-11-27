"""
This module defines a data structure for representing information about a token.

The `TokenInfo` class provides a convenient way to store and access details about a 
token, including its contract type, name, symbol, and other relevant metadata. 
This can be useful in blockchain applications, token explorers, or any system 
requiring structured information about tokens.

The module leverages Python's `dataclasses` module to simplify class construction 
and improve code readability.
"""

from dataclasses import dataclass


@dataclass
class TokenInfo:
    """
    A data class that encapsulates metadata about a token.

    Attributes:
        contract_type (str): The type of token contract (e.g., ERC-20, ERC-721).
        name (str): The name of the token.
        symbol (str): The symbol representing the token (e.g., "ETH", "BTC").
        icon (str): A URL or file path to the token's icon image.
        decimal (int): The number of decimal places the token supports.
        total_supply (int): The total supply of the token.
        total_transfers (int): The total number of transfers involving the token.
        official_site (str): The official website URL for the token or project.
        burn_amount (int): The total amount of the token that has been burned.
        total_burns (int): The total number of burn transactions.
    """

    contract_type: str
    name: str
    symbol: str
    icon: str
    decimal: int
    total_supply: int
    total_transfers: int
    official_site: str
    burn_amount: int
    total_burns: int
