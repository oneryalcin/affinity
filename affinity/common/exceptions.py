from __future__ import annotations


class TokenMissing(Exception):
    pass


class RequestTypeNotAllowed(Exception):
    pass


class RequestFailed(Exception):
    """ An exception raised when a request fails """
    def __init__(self, message: str | bytes, status_code: int):
        self.message = message
        self.status_code = status_code
    pass


class RequiredPayloadFieldMissing(Exception):
    pass


class RequiredQueryParamMissing(Exception):
    pass


class ClientError(Exception):
    pass
