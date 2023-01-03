from argparse import ArgumentParser
from sheep import sheep


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("user")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    sheep(args.domain, args.user, verbose=args.verbose)
