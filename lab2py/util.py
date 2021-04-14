

def complementary_literals(literal1: str, literal2: str):
    if len(literal1) > len(literal2):
        return literal1[1:] == literal2
    else:
        return literal1 == literal2[1:]


def get_atom(literal: str):
    return literal[1:] if literal[0] == '~' else literal


def remove_irrelevant(clauses: []):
    return [clause for clause in clauses if not is_tautology(clause)]


def remove_redundant(clauses: []):
    return [c1 for c1 in clauses if not any(c1 < c2 for c2 in clauses)]


def is_tautology(clause):
    for (c1, c2) in clause:
        if complementary_literals(c1, c2):
            return True

    return False
