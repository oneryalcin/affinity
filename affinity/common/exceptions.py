from __future__ import annotations

from typing import Optional


class AffinityBaseException(Exception):
    pass


class TokenMissing(AffinityBaseException):
    pass


class RequestTypeNotAllowed(AffinityBaseException):
    pass


class RequestFailed(AffinityBaseException):
    """ An exception raised when a request fails """
    def __init__(self, message: str, status_code: Optional[int] = None, response: dict | None = None):
        self.message = message
        self.response = response
        self.status_code = status_code
    pass


class RateLimitExceeded(AffinityBaseException):
    """ An exception raised when a rate limit is exceeded """
    def __init__(self, message: str, retry_after: int | None = None, response: dict | None = None):
        self.message = message
        self.response = response
        self.retry_after = retry_after


class RequiredPayloadFieldMissing(AffinityBaseException):
    pass


class RequiredQueryParamMissing(AffinityBaseException):
    pass


class ClientError(AffinityBaseException):
    pass
