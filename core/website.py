from dataclasses import dataclass, field
from typing import List

import requests

@dataclass
class Website:
    """
    Representing a website.

    :param name: name of the website.
    :param url: URL of the website object.
    :param status_code: status code of the website.
    """
    name: str
    url: str
    status_code: int = 0

    def get_status_code(self) -> int:
        """
        Return status code of a site.

        :return: a status code of a site
        :rtype: int
        """
        response = requests.get(self.url, timeout=3)
        return response.status_code

    def get_headers(self) -> str:
        """
        Return headers of a site.

        :return: headers of a site
        :rtype: str
        """
        response = requests.get(self.url, timeout=3)
        return response.headers


class UpdateWebsiteStatusCode:
    """
    Command that update status codes of a website.
    """
    def __init__(self, website):
        self.website = website

    def execute(self):
        self.website.status_code = self.website.get_status_code()


def init_websites(sites) -> List:
    """
    Turn the dict of sites into Website objects.
    """
    websites = [] # a list of website objects converted from a dict
    for k, v in sites.items():
        websites.append(Website(k, v))

    return websites

def update_website_status(sites) -> None:
    """
    Check status and update the status of sites.
    """
    for site in sites:
        site.status_code = site.get_status_code()