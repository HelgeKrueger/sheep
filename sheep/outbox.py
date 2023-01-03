from rich import print as pprint

from .activity_json_fetcher import ActivityJsonFetcher


class Outbox(ActivityJsonFetcher):
    def __init__(self, link, verbose=False):
        self.verbose = verbose

        self.data_base = self.fetch_base(link)

    def fetch_base(self, url):
        return self.fetch_activity_json(url)

    def first_page(self):
        first_page = self.data_base["first"]

        if self.verbose:
            pprint(f"Fetching first page of outbox from {first_page}")

        return self.fetch_activity_json(first_page)
