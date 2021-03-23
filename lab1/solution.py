# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import loader
import args_parser


def main():

    print(args_parser.args)

    print(loader.state_space_loader(args_parser.args.ss))
    print(loader.heuristic_loader(args_parser.args.h))


main()
