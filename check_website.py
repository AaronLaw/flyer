# Check sites
# Reference:
#     https://realpython.com/python-requests/

from typing import List
from core.website import Website
from core.website import init_websites, update_website_status

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

def display_status_code(sites) -> None:
    for site in sites:
        print(f'{site.name} => {site.status_code}')

if __name__ == "__main__":
    main()
