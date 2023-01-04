from rich import print as pprint
from rich.table import Table

from inscriptis import get_text


def interact_with_outbox(content):
    pprint("---- Outbox ----")
    pprint(f"{len(content)} items in outbox")

    display_table(content)

    pprint("Type in number of id to display object")

    while True:
        answer = input("Id or 'q': ")
        if answer == "q":
            return

        if answer.startswith("r"):
            idx = int(answer[1:])
            pprint(content[idx])
        else:
            idx = int(answer)
            pprint(content[idx]["object"])


def display_table(content):
    table = Table(title="Activities in Outbox", min_width=50)

    table.add_column("Id")
    table.add_column("Activity Type")
    table.add_column("Object")
    table.add_column("Content")

    for idx, x in enumerate(content):
        text = ""
        obj = x["object"]

        if isinstance(obj, str):
            if obj.startswith("https://"):
                obj = f"[link={obj}]url[/link]"
        elif isinstance(obj, dict):
            text = get_text(obj["content"]).replace("\n", " ").strip()[:60]
            obj = f"Type: {obj['type']}"

        table.add_row(str(idx), x["type"], obj, text)

    pprint(table)
