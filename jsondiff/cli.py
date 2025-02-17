import argparse
import jsondiff
import json
import warnings
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first")
    parser.add_argument("second")
    parser.add_argument("-p", "--patch", action="store_true", default=False)
    parser.add_argument("-s", "--syntax", action="store", type=str, default="compact")
    parser.add_argument("-i", "--indent", action="store", type=int, default=None)
    parser.add_argument("-l", "--list_as_set", action="store", type=bool, default=False)

    args = parser.parse_args()

    with open(args.first, "r") as f:
        with open(args.second, "r") as g:
            jf = json.load(f)
            jg = json.load(g)
            if args.patch:
                x = jsondiff.patch(
                    jf,
                    jg,
                    marshal=True,
                    syntax=args.syntax,
                    list_as_set=args.list_as_set
                )
            else:
                x = jsondiff.diff(
                    jf,
                    jg,
                    marshal=True,
                    syntax=args.syntax,
                    list_as_set=args.list_as_set
                )

            json.dump(x, sys.stdout, indent=args.indent)


if __name__ == '__main__':
    main()
