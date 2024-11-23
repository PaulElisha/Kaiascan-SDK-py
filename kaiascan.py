import os
import requests
from urllib.parse import urlencode

class KaiascanSDK:
    def __init__(self, is_testnet: bool):
        self.chain_info = {
            "BASE_URL_TESTNET": "https://testnet.example.com/",
            "BASE_URL_MAINNET": "https://mainnet.example.com/",
            "CHAIN_ID_TESTNET": "testnet_chain_id",
            "CHAIN_ID_MAINNET": "mainnet_chain_id"
        }
        
        if is_testnet:
            self.BASE_URL = self.chain_info["BASE_URL_TESTNET"]
            self.CHAIN_ID = self.chain_info["CHAIN_ID_TESTNET"]
        else:
            self.BASE_URL = self.chain_info["BASE_URL_MAINNET"]
            self.CHAIN_ID = self.chain_info["CHAIN_ID_MAINNET"]

    def _fetch_api(self, url: str):
        headers = {
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
            "Content-Type": "application/json",
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            api_response = response.json()
            
            if api_response.get("code") != 0:
                raise Exception(f"API error! code: {api_response['code']}, message: {api_response['msg']}")
            
            return api_response
        except requests.RequestException as e:
            raise Exception(f"Error making request to {url}: {e}")

    def get_account_key_histories(self, account_address: str, page: int = 1, size: int = 20):
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not (1 <= size <= 2000):
            raise ValueError("Size must be between 1 and 2000")
        
        query_params = {"page": page, "size": size}
        url = f"{self.BASE_URL}api/v1/accounts/{account_address}/key-histories?{urlencode(query_params)}"
        return self._fetch_api(url)

    def get_kaia_info(self):
        url = f"{self.BASE_URL}api/v1/kaia"
        return self._fetch_api(url)

    def get_fungible_token(self, token_address: str):
        url = f"{self.BASE_URL}tokens?tokenAddress={token_address}"
        return self._fetch_api(url)

    def get_nft_item(self, nft_address: str, token_id: str):
        url = f"{self.BASE_URL}nfts?{urlencode({'nftAddress': nft_address, 'tokenId': token_id})}"
        return self._fetch_api(url)

    def get_contract_creation_code(self, contract_address: str):
        url = f"{self.BASE_URL}contracts/creation-code?contractAddress={contract_address}"
        return self._fetch_api(url)

    def get_contract_source_code(self, contract_address: str):
        url = f"{self.BASE_URL}contracts/source-code?contractAddress={contract_address}"
        return self._fetch_api(url)

    def get_latest_block(self):
        url = f"{self.BASE_URL}blocks/latest"
        return self._fetch_api(url)

    def get_latest_block_burns(self, page: int = 1, size: int = 20):
        if page < 1 or not (1 <= size <= 2000):
            raise ValueError("Page and size must meet criteria")
        
        query_params = {"page": page, "size": size}
        url = f"{self.BASE_URL}blocks/latest/burns?{urlencode(query_params)}"
        return self._fetch_api(url)

    def get_block(self, block_number: int):
        url = f"{self.BASE_URL}blocks?blockNumber={block_number}"
        return self._fetch_api(url)

    def get_transactions_of_block(self, block_number: int, tx_type: str = None, page: int = 1, size: int = 20):
        query_params = {"page": page, "size": size}
        if tx_type:
            query_params["type"] = tx_type
        
        url = f"{self.BASE_URL}blocks/{block_number}/transactions?{urlencode(query_params)}"
        return self._fetch_api(url)

    def get_transaction(self, transaction_hash: str):
        url = f"{self.BASE_URL}transactions/{transaction_hash}"
        return self._fetch_api(url)

    def get_transaction_receipt_status(self, transaction_hash: str):
        url = f"{self.BASE_URL}transaction-receipts/status?transactionHash={transaction_hash}"
        return self._fetch_api(url)

    def get_transaction_status(self, transaction_hash: str):
        url = f"{self.BASE_URL}transactions/{transaction_hash}/status"
        return self._fetch_api(url)
