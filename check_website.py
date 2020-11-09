# Check sites
# Reference:
#     https://realpython.com/python-requests/
import requests

sites = {
    'Google':   'https://www.google.com',
    'Yahoo':    'https://www.yahoo.com',
    'YouTube':  'https://www.youtube.com'
    }

for k, v in sites.items():
    # print(f'{k} -> {v}')
    response = requests.get(v)
    print(f'{k} => {response.status_code}')
    