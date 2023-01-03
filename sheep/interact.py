from rich import print as pprint

from rich.table import Table


def interact_with_outbox(content):
    pprint("---- Outbox ----")
    pprint(f"{len(content)} items in outbox")

    display_table(content)

    pprint("Type in number of id to display object")

    while True:
        answer = input("Id or 'q': ")
        if answer == "q":
            return

        idx = int(answer)

        pprint(content[idx]["object"])


def display_table(content):
    table = Table(title="Activities in Outbox", min_width=50)

    table.add_column("Id")
    table.add_column("Type")

    for idx, x in enumerate(content):
        table.add_row(str(idx), x["type"])

    pprint(table)
