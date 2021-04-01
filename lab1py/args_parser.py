import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--alg', type=str)
parser.add_argument('--ss', type=str)
parser.add_argument('--h', type=str)
parser.add_argument('--check-optimistic', action='store_true')
parser.add_argument('--check-consistent', action='store_true')

args = parser.parse_args()


