# Check sites
# Reference:
#     https://realpython.com/python-requests/

from typing import List
from core.website import Website
from core.website import InitializeWebsites, UpdateWebsitesStatus

import requests

sites = {
    'Google':   'https://www.google.com',
    'NON existing Google':'https://www.nogoogle.com', # site that doesn't exist
    'Yahoo':    'https://www.yahoo.com',
    'YouTube':  'https://www.youtube.com'
    }

websites = {} # class variable shared by all instances


def main():
    websites = InitializeWebsites(sites).execute()
    UpdateWebsitesStatus(websites).execute()
    display_status_code(websites)

def display_status_code(sites) -> None:
    for count, site in enumerate(sites):
        print(f'{count}. {site.name} => {site.status_code}')

if __name__ == "__main__":
    main()
