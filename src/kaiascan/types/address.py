"""
This module provides a custom type and helper function for handling blockchain addresses.

The `Address` type is a custom type alias for representing blockchain addresses, 
making code more readable and type-safe. It leverages Python's `NewType` from the `typing` 
module to differentiate addresses from regular strings.

The module also includes a utility function `is_valid_address` to validate if a given 
string conforms to the expected format of a blockchain address (e.g., starting with "0x").

Usage:
    Use the `Address` type for function arguments, return values, or variables 
    where blockchain addresses are expected. The `is_valid_address` function 
    can be used to validate addresses before processing.
"""

from typing import NewType

# Creating a custom type for addresses
Address = NewType("Address", str)


# Type validation helper
def is_valid_address(addr: str) -> bool:
    """
    Validates whether a given string is a valid blockchain address.

    A valid blockchain address is a string that:
        1. Is an instance of `str`.
        2. Starts with the prefix "0x".

    Args:
        addr (str): The string to validate as a blockchain address.

    Returns:
        bool: `True` if the input is a valid blockchain address, otherwise `False`.
    """
    return isinstance(addr, str) and addr.startswith("0x")
