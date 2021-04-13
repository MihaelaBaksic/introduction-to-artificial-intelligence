import argparse

parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('path_clauses', type=str)
parser.add_argument('path_user_commands', type=str, nargs='?')

args = parser.parse_args()
