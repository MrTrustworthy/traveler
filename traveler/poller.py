
import requests


class Poller:
    """
    Test documentation
    """

    def __init__(self):
        """ Init function

        Arguments:
            self The object. Object.
        """
        self.schema = 'https://'
        self.base_url = 'www.google.com'

    def load(self):
        """ Load function

        Arguments:
            self The object. Object.
        """

        res = requests.get(self.schema + self.base_url)

        res.raise_for_status()

        return res.text
