#!/usr/bin/env python

"""Tests for `kaiascan_sdk_py` package."""

# import pytest

from kaiascan import kaiascan


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_sdk_initialization():
    """Test the Testnet initialization"""
    sdk = kaiascan.KaiascanSDK(is_testnet=True)
    assert sdk.base_url == "https://kairos-oapi.kaiascan.io/"
    assert sdk.chain_id == "1001"


def test_sdk_mainnet_initialization():
    """Test the Mainnet initialization"""
    sdk = kaiascan.KaiascanSDK(is_testnet=False)
    assert sdk.base_url == "https://mainnet-oapi.kaiascan.io/"
    assert sdk.chain_id == "8217"


def test_token_info():
    """Test the TokenInfo data class."""
    from kaiascan.interfaces.token_info import TokenInfo

    token = TokenInfo(
        contract_type="ERC-20",
        name="Kaia Token",
        symbol="KAIA",
        icon="https://example.com/icon.png",
        decimal=18,
        total_supply=1000000,
        total_transfers=500,
        official_site="https://kaiaproject.io",
        burn_amount=1000,
        total_burns=10,
    )

    assert token.contract_type == "ERC-20"
    assert token.name == "Kaia Token"
    assert token.symbol == "KAIA"
    assert token.icon == "https://example.com/icon.png"
    assert token.decimal == 18
    assert token.total_supply == 1000000
    assert token.total_transfers == 500
    assert token.official_site == "https://kaiaproject.io"
    assert token.burn_amount == 1000
    assert token.total_burns == 10


def test_endpoints():
    """Test the ENDPOINTS dictionary."""
    from kaiascan.objects.endpoints import ENDPOINTS

    assert ENDPOINTS["tokens_endpoint"] == "api/v1/tokens"
    assert ENDPOINTS["nfts_endpoint"] == "api/v1/nfts"
    assert ENDPOINTS["blocks_endpoint"] == "api/v1/blocks"
    assert ENDPOINTS["transaction_endpoint"] == "api/v1/transactions"
    assert ENDPOINTS["contract_endpoint"] == "api/v1/contracts"
    assert ENDPOINTS["transaction_receipts_endpoint"] == "api/v1/transaction-receipts"


def test_chain_info():
    """Test the CHAIN_INFO dictionary."""
    from kaiascan.objects.chain_info import CHAIN_INFO

    assert CHAIN_INFO["BASE_URL_MAINNET"] == "https://mainnet-oapi.kaiascan.io/"
    assert CHAIN_INFO["BASE_URL_TESTNET"] == "https://kairos-oapi.kaiascan.io/"
    assert CHAIN_INFO["CHAIN_ID_MAINNET"] == "8217"
    assert CHAIN_INFO["CHAIN_ID_TESTNET"] == "1001"


def test_api_response():
    """Test the ApiResponse class."""
    from kaiascan.interfaces.api_response import ApiResponse

    response = ApiResponse(code=200, data={"key": "value"}, msg="Success")

    assert response.code == 200
    assert response.data == {"key": "value"}
    assert response.msg == "Success"


def test_address_validation():
    """Test the is_valid_address function."""
    from kaiascan.types.address import is_valid_address

    valid_address = "0x1234567890abcdef"
    invalid_address = "1234567890abcdef"

    assert is_valid_address(valid_address) is True
    assert is_valid_address(invalid_address) is False
