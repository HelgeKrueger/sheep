from rich import print as pprint

from .webfinger import Webfinger
from .actor import Actor
from .outbox import Outbox

from .interact import interact_with_outbox


def sheep(domain, user, verbose=False, display_user=False):
    webfinger = Webfinger(domain, user, verbose=verbose)

    link_to_self = webfinger.get_self()

    actor = Actor(link_to_self, verbose=verbose)

    if display_user:
        pprint(actor.data)
        return

    outbox = Outbox(actor.get_outbox(), verbose=verbose)

    first_page = outbox.first_page()

    interact_with_outbox(first_page["orderedItems"])
