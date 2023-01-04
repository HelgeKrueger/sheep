from argparse import ArgumentParser
from sheep import sheep


if __name__ == "__main__":
    parser = ArgumentParser()
    # parser.add_argument("domain")
    parser.add_argument("user", help="e.g. helge@mas.to")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--display_user", action="store_true")
    args = parser.parse_args()

    user_name = args.user
    if user_name[0] == "@":
        user_name = user_name[1:]

    _, domain = user_name.split("@")

    sheep(domain, user_name, verbose=args.verbose, display_user=args.display_user)
