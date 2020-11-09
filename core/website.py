import requests

class Website:
    """
    Representing a website
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.status_code
        
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
