import itertools


def complement(c):
    return '~' + c if c[0] != '~' else c[1:]


def negate(c):
    return '~' + c


def get_atom(literal: str):
    return literal[1:] if literal[0] == '~' else literal


def remove_irrelevant(clauses: set):
    return {clause for clause in clauses if not is_tautology(clause)}


def remove_redundant(clauses: set):
    return {c1 for c1 in clauses if not any(c1 >= c2 and c1 != c2 for c2 in clauses)}


def is_tautology(clause):
    for c1, c2 in itertools.combinations(clause, 2):
        if negate(c1) in c2:
            return True
    return False


def is_subset(l1, l2):
    for elem in l1:
        if elem not in l2:
            return False

    return True
