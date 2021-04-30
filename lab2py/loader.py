from util import complement


def load_clauses(path: str):
    clauses = []
    with open(path) as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            clauses.append({x.strip() for x in line.lower().split(' v')})

    return negate_goal(clauses[-1]), clauses[0:-1]


def load_commands(path: str):
    commands = []


def negate_goal(goals):
    return [{complement(atom)} for atom in goals]


