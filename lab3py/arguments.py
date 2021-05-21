import argparse

parser = argparse.ArgumentParser()
parser.add_argument('training', type=str)
parser.add_argument('test', type=str)
parser.add_argument('depth', type=int, nargs='?')


args = parser.parse_args()
