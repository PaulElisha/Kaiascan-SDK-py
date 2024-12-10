from typing import Optional, Any, TypeVar, List
import os
import urllib.parse
from requests import Session
from .objects.chain_info import CHAIN_INFO
from .objects.endpoints import ENDPOINTS
from .interfaces.api_response import ApiResponse
from .interfaces.token_info import TokenInfo
from .types.address import Address

T = TypeVar("T")


class KaiascanSDK:
    def __init__(self, is_testnet: bool):
        self.base_url = (
            CHAIN_INFO["BASE_URL_TESTNET"]
            if is_testnet
            else CHAIN_INFO["BASE_URL_MAINNET"]
        )
        self.chain_id = (
            CHAIN_INFO["CHAIN_ID_TESTNET"]
            if is_testnet
            else CHAIN_INFO["CHAIN_ID_MAINNET"]
        )
        self.session = Session()
        self.session.headers.update(
            {
                "Authorization": f'Bearer {os.getenv("API_KEY")}',
                "Content-Type": "application/json",
            }
        )

    def _fetch_api(self, url_str: str) -> ApiResponse[T]:
        try:
            response = self.session.get(url_str)
            response.raise_for_status()
            data = response.json()

            api_response = ApiResponse(
                code=data["code"], data=data["data"], msg=data["msg"]
            )

            if api_response.code != 0:
                raise Exception(
                    f"API error! code: {api_response.code}, message: {api_response.msg}"
                )

            return api_response
        except Exception as error:
            raise Exception(f"Error making request to {url_str}: {str(error)}")

    def get_account_key_histories(
        self, account_address: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/accounts/{urllib.parse.quote(account_address)}/key-histories?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_info(self, account_address: str) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}"
        return self._fetch_api(url_str)

    def get_account_token_transfers(
        self,
        account_address: str,
        page: int = 1,
        size: int = 20,
        contract_address: Optional[str] = None,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if contract_address:
            query_params.append(f"contractAddress={contract_address}")
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}/token-transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_event_logs(
        self,
        account_address: str,
        page: int = 1,
        size: int = 20,
        signature: Optional[str] = None,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if signature:
            query_params.append(f"signature={signature}")
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}/event-logs?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_kip17_nft_balances(
        self, account_address: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/accounts/{account_address}/nft-balances/kip17?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_kip37_nft_balances(
        self, account_address: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/accounts/{account_address}/nft-balances/kip37?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_nft_transfers(
        self,
        account_address: str,
        page: int = 1,
        size: int = 20,
        contract_address: Optional[str] = None,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if contract_address:
            query_params.append(f"contractAddress={contract_address}")
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}/nft-transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_token_balances(
        self, account_address: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/accounts/{account_address}/token-balances?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_token_details(
        self, account_address: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/accounts/{account_address}/token-details?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_account_transactions(
        self,
        account_address: str,
        page: int = 1,
        size: int = 20,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
        transaction_type: Optional[str] = None,
        directions: Optional[List[str]] = None,
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")
        if transaction_type:
            query_params.append(f"type={transaction_type}")
        if directions:
            query_params.append(f"directions={','.join(directions)}")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}/transactions?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_fee_paid_transactions(
        self,
        account_address: str,
        page: int = 1,
        size: int = 20,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
        transaction_type: Optional[str] = None,
    ) -> ApiResponse[Any]:
        if not account_address:
            raise ValueError("Account address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")
        if transaction_type:
            query_params.append(f"type={transaction_type}")

        url_str = f"{self.base_url}api/v1/accounts/{account_address}/fee-paid-transactions?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_kaia_info(self) -> ApiResponse[Any]:
        url_str = f"{self.base_url}api/v1/kaia"
        return self._fetch_api(url_str)

    def get_fungible_token(self, token_address: Address) -> ApiResponse[TokenInfo]:
        url_str = f"{self.base_url}{ENDPOINTS['tokens_endpoint']}?tokenAddress={urllib.parse.quote(token_address)}"
        return self._fetch_api(url_str)

    def get_token_holders(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        holder_address: Optional[str] = None,
    ) -> ApiResponse[Any]:
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if holder_address:
            query_params.append(f"holderAddress={holder_address}")

        url_str = f"{self.base_url}api/v1/tokens/{token_address}/holders?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_token_burns(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/tokens/{token_address}/burns?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_token_transfers(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/tokens/{token_address}/transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_nft_item(self, nft_address: Address, token_id: str) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['nfts_endpoint']}?nftAddress={urllib.parse.quote(nft_address)}&tokenId={urllib.parse.quote(token_id)}"
        return self._fetch_api(url_str)

    def get_nft(self, token_address: str) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")

        url_str = f"{self.base_url}api/v1/nfts/{token_address}"
        return self._fetch_api(url_str)

    def get_nft_transfers(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        token_id: Optional[str] = None,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
    ) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if token_id:
            query_params.append(f"tokenId={token_id}")
        if block_number_start:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end:
            query_params.append(f"blockNumberEnd={block_number_end}")

        url_str = f"{self.base_url}api/v1/nfts/{token_address}/transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_nft_holders(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        token_id: Optional[str] = None,
    ) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if token_id:
            query_params.append(f"tokenId={token_id}")

        url_str = f"{self.base_url}api/v1/nfts/{token_address}/holders?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_nft_inventories(
        self,
        token_address: str,
        page: int = 1,
        size: int = 20,
        keyword: Optional[str] = None,
    ) -> ApiResponse[Any]:
        if not token_address:
            raise ValueError("Token address is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if keyword:
            query_params.append(f"keyword={keyword}")

        url_str = f"{self.base_url}api/v1/nfts/{token_address}/inventories?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_contract_creation_code(self, contract_address: Address) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['contract_endpoint']}/creation-code?contractAddress={urllib.parse.quote(contract_address)}"
        return self._fetch_api(url_str)

    def get_contract_source_code(self, contract_address: Address) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['contract_endpoint']}/source-code?contractAddress={urllib.parse.quote(contract_address)}"
        return self._fetch_api(url_str)

    def get_contract_info(self, contract_address: str) -> ApiResponse[Any]:
        if not contract_address:
            raise ValueError("Contract address is required")

        url_str = f"{self.base_url}api/v1/contracts/{contract_address}"
        return self._fetch_api(url_str)

    def get_contracts_info(self, contract_addresses: List[str]) -> ApiResponse[Any]:
        if not contract_addresses or len(contract_addresses) == 0:
            raise ValueError("Contract address list is required")

        query_params = f"contractAddresses={','.join(contract_addresses)}"
        url_str = f"{self.base_url}api/v1/contracts?{query_params}"
        return self._fetch_api(url_str)

    def get_contract_abi(self, contract_address: str) -> ApiResponse[Any]:
        if not contract_address:
            raise ValueError("Contract address is required")

        url_str = f"{self.base_url}api/v1/contracts/{contract_address}/abi"
        return self._fetch_api(url_str)

    def get_latest_block(self) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['blocks_endpoint']}/latest"
        return self._fetch_api(url_str)

    def get_latest_block_burns(self, page: int = 1, size: int = 20) -> ApiResponse[Any]:
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/blocks/latest/burns?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_latest_block_rewards(self, block_number: int) -> ApiResponse[Any]:
        url_str = (
            f"{self.base_url}api/v1/blocks/latest/rewards?blockNumber={block_number}"
        )
        return self._fetch_api(url_str)

    def get_block(self, block_number: int) -> ApiResponse[Any]:
        url_str = (
            f"{self.base_url}{ENDPOINTS['blocks_endpoint']}?blockNumber={block_number}"
        )
        return self._fetch_api(url_str)

    def get_blocks(
        self,
        block_number: int,
        block_number_start: Optional[int] = None,
        block_number_end: Optional[int] = None,
        page: int = 1,
        size: int = 20,
    ) -> ApiResponse[Any]:
        query_params = []

        if block_number_start is not None:
            query_params.append(f"blockNumberStart={block_number_start}")
        if block_number_end is not None:
            query_params.append(f"blockNumberEnd={block_number_end}")
        if page >= 1:
            query_params.append(f"page={page}")
        if 1 <= size <= 2000:
            query_params.append(f"size={size}")

        url_str = (
            f"{self.base_url}{ENDPOINTS['blocks_endpoint']}?blockNumber={block_number}"
            f"{'&' + '&'.join(query_params) if query_params else ''}"
        )
        return self._fetch_api(url_str)

    def get_transactions_of_block(
        self,
        block_number: int,
        transaction_type: Optional[str] = None,
        page: int = 1,
        size: int = 20,
    ) -> ApiResponse[Any]:
        query_params = []

        if transaction_type:
            query_params.append(f"type={urllib.parse.quote(transaction_type)}")
        if page >= 1:
            query_params.append(f"page={page}")
        if 1 <= size <= 2000:
            query_params.append(f"size={size}")

        url_str = (
            f"{self.base_url}{ENDPOINTS['blocks_endpoint']}/{block_number}/transactions"
            f"{'?' + '&'.join(query_params) if query_params else ''}"
        )
        return self._fetch_api(url_str)

    def get_block_burns(self, block_number: int) -> ApiResponse[Any]:
        url_str = f"{self.base_url}api/v1/blocks/{block_number}/burns"
        return self._fetch_api(url_str)

    def get_block_rewards(self, block_number: int) -> ApiResponse[Any]:
        url_str = f"{self.base_url}api/v1/blocks/{block_number}/rewards"
        return self._fetch_api(url_str)

    def get_internal_transactions_of_block(
        self, block_number: int, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/blocks/{block_number}/internal-transactions?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_blocks_by_timestamp(self, timestamp: int) -> ApiResponse[Any]:
        if timestamp <= 0:
            raise ValueError("Timestamp must be a positive integer")

        url_str = f"{self.base_url}api/v1/blocks/timestamps/{timestamp}"
        return self._fetch_api(url_str)

    def get_transaction(self, transaction_hash: str) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['transaction_endpoint']}/{urllib.parse.quote(transaction_hash)}"
        return self._fetch_api(url_str)

    def get_transaction_receipt_status(self, transaction_hash: str) -> ApiResponse[Any]:
        url_str = f"{self.base_url}{ENDPOINTS['transaction_receipts_endpoint']}/status?transactionHash={urllib.parse.quote(transaction_hash)}"
        return self._fetch_api(url_str)

    def get_transaction_status(self, transaction_hash: str) -> ApiResponse[Any]:
        url_str = f"{self.base_url}api/v1/transactions/{urllib.parse.quote(transaction_hash)}/status"
        return self._fetch_api(url_str)

    def get_transaction_input_data(self, transaction_hash: str) -> ApiResponse[Any]:
        if not transaction_hash:
            raise ValueError("Transaction hash is required")

        url_str = f"{self.base_url}api/v1/transactions/{transaction_hash}/input-data"
        return self._fetch_api(url_str)

    def get_transaction_event_logs(
        self,
        transaction_hash: str,
        page: int = 1,
        size: int = 20,
        signature: Optional[str] = None,
    ) -> ApiResponse[Any]:
        if not transaction_hash:
            raise ValueError("Transaction hash is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        if signature:
            query_params.append(f"signature={signature}")

        url_str = f"{self.base_url}api/v1/transactions/{transaction_hash}/event-logs?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_transaction_internal_transactions(
        self, transaction_hash: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not transaction_hash:
            raise ValueError("Transaction hash is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/transactions/{transaction_hash}/internal-transactions?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_transaction_token_transfers(
        self, transaction_hash: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not transaction_hash:
            raise ValueError("Transaction hash is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/transactions/{transaction_hash}/token-transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)

    def get_transaction_nft_transfers(
        self, transaction_hash: str, page: int = 1, size: int = 20
    ) -> ApiResponse[Any]:
        if not transaction_hash:
            raise ValueError("Transaction hash is required")
        if page < 1:
            raise ValueError("Page must be >= 1")
        if not 1 <= size <= 2000:
            raise ValueError("Size must be between 1 and 2000")

        query_params = [f"page={page}", f"size={size}"]
        url_str = f"{self.base_url}api/v1/transactions/{transaction_hash}/nft-transfers?{'&'.join(query_params)}"
        return self._fetch_api(url_str)
