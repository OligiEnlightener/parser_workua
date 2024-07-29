# import requests
from fake_useragent import UserAgent
from requests import Response, get


class RequestEngine:
    def get_response(self, url: str, params: dict | None) -> Response:
        headers = {"User-Agent": UserAgent(platforms='pc').random}
        return get(url=url, params=params, headers=headers)
