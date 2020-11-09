# Check sites
# Reference:
#     https://realpython.com/python-requests/

from typing import List
from core.website import Website

import requests

sites = {
    'Google':   'https://www.google.com',
    'Yahoo':    'https://www.yahoo.com',
    'YouTube':  'https://www.youtube.com'
    }

websites = {} # class variable shared by all instances


def main():
    websites = init_websites(sites)
    update_website_status(websites)
    display_status_code(websites)

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

def display_status_code(sites) -> None:
    for site in sites:
        print(f'{site.name} => {site.status_code}')

if __name__ == "__main__":
    main()
