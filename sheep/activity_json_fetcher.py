import requests

from rich import print as pprint


class ActivityJsonFetcher:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def fetch_activity_json(self, url):
        response = requests.get(url, headers={"Accept": "application/activity+json"})

        if not response.ok:
            pprint()
            pprint("----HEADERS----")
            pprint(response.headers)
            pprint()
            pprint("----DATA----")
            pprint(response.text)
            pprint("")
            exit(1)

        if self.verbose:
            pprint()
            pprint("----HEADERS----")
            pprint(response.headers)
            pprint()
            pprint("----DATA----")
            pprint(response.json())
            pprint("")

        return response.json()
