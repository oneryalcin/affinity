import datetime as dt
import requests as r
from enums import Enum
from typing import List, Dict, Optional
from affinity.common.exceptions import TokenMissing, RequestTypeNotAllowed

BASE_URL = "https://api.affinity.co"

class RequestType:
    GET: 1
    LIST: 2
    CREATE: 3
    DELETE: 4

class Endpoint:
    endpoint: str = None
    request_types: List[RequestType] = []

    def __init__(self, token: str):
        self.token = token

    def get(self, id: int):
        if not self.token:
            raise TokenMissing
        if RequestType.GET not in self.request_types:
            raise RequestTypeNotAllowed
        return r.get(url=f"{BASE_URL}/{self.endpoint}/{id}", auth=(None, self.token))

    def list(self):
        if not self.token:
            raise TokenMissing
         if RequestType.LIST not in self.request_types:
            raise RequestTypeNotAllowed
        return r.get(url=f"{BASE_URL}/{self.endpoint}", auth=(None, self.token))
        
    def create(self, data):
        if not self.token:
            raise TokenMissing
        if RequestType.CREATE not in self.request_types:
            raise RequestTypeNotAllowed
       headers = {"Content-Type" : "application/json"}
        return r.post(url=f"{BASE_URL}/{self.endpoint}", data=data, headers=headers, auth=(None, self.token))

    def delete(self, id):
        if not self.token:
            raise TokenMissing
        if RequestType.DELETE not in self.request_types:
            raise RequestTypeNotAlllowed
        return r.delete(url=f"{BASE_URL}/{self.endpoint}")

class Lists(Endpoint):
    endpoint = "lists"
    request_types: [RequestType.GET, RequestType.LIST]
