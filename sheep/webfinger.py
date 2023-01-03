from rich import print as pprint

from .activity_json_fetcher import ActivityJsonFetcher


class Webfinger(ActivityJsonFetcher):
    def __init__(self, domain, user, verbose=False):
        self.verbose = verbose

        self.data = self.fetch(domain, user)

    def get_self(self):
        links = self.data["links"]

        for l in links:
            if l["rel"] == "self":
                if l["type"] != "application/activity+json":
                    pprint(f"Got type {l['type']} for self link")

                return l["href"]

    def fetch(self, domain, user):
        url = f"https://{domain}/.well-known/webfinger?resource=acct:{user}"

        if self.verbose:
            pprint(f"Fetching webfinger from {url}")

        return self.fetch_activity_json(url)
