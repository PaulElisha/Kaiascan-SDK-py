"""API response interface for standardized return types."""

from typing import TypeVar, Generic

T = TypeVar("T")


class ApiResponse(Generic[T]):
    """
    A generic class for representing API responses.

    Attributes:
        code (int): The status code of the API response (e.g., HTTP status codes).
        data (T): The payload of the response, which can be any type.
        msg (str): A message describing the result of the API call, such as "Success" or "Error".

    Generic Type:
        T: The type of the data payload, allowing flexibility for various use cases.
    """

    def __init__(self, code: int, data: T, msg: str):
        self.code: int = code
        self.data: T = data
        self.msg: str = msg
