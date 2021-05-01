from util import complement


def load_clauses(path: str):
    clauses = []
    with open(path) as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            clauses.append(frozenset({x.strip() for x in line.lower().split(' v')}))

    return clauses[-1], negate_goal(clauses[-1]), set(clauses[0:-1])


def load_commands(path_r: str, path_c: str):
    clauses = []
    with open(path_r) as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            clauses.append(frozenset({x.strip() for x in line.lower().split(' v')}))

    commands = []
    with open(path_c) as f:
        for line in f:
            if line.strip()[0] != '#':
                line = line.strip()
                clause = frozenset({x.strip() for x in line.lower()[:-2].split(' v')})
                command = line[-1]
                commands.append((clause, command))

    # print(clauses)
    # print(commands)
    # print('____________________')
    return set(clauses), commands


def negate_goal(goals):
    return {frozenset({complement(atom)}) for atom in goals}


