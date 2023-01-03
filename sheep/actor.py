from rich import print as pprint

from .activity_json_fetcher import ActivityJsonFetcher


class Actor(ActivityJsonFetcher):
    def __init__(self, link, verbose=False):
        self.verbose = verbose

        self.data = self.fetch(link)

    def get_outbox(self):
        return self.data["outbox"]

    def fetch(self, link):
        if self.verbose:
            pprint(f"Fetching actor from {link}")

        return self.fetch_activity_json(link)
