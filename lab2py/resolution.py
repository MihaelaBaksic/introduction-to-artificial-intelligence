from util import *


def resolution(premises: list, neg_goal: list):
    knowledge = remove_redundant(remove_irrelevant(premises))
    set_of_support = neg_goal

    while True:
        new = []
        for c1, c2 in select_clauses(set_of_support, knowledge):
            res = remove_irrelevant(resolve(c1, c2))
            print(str(c1) + ' + ' + str(c2) + ' = ' + str(res))
            if set() in res:
                return True

            new.extend(res)

        if all(r in knowledge + set_of_support for r in new):
            return False

        knowledge = remove_redundant(remove_irrelevant(knowledge + set_of_support))
        set_of_support = remove_redundant(remove_irrelevant(new))


def select_clauses(sos, knowledge):
    # at least one in the pair should come from set of support
    selected_clauses = []

    second = sos + knowledge

    for clause1 in sos:
        for clause2 in second:
            if can_be_resolved(clause1, clause2) and (clause2, clause1) not in selected_clauses:
                selected_clauses.append((clause1, clause2))

    return selected_clauses


def can_be_resolved(c1, c2):
    for a1 in c1:
        if complement(a1) in c2:
            return True

    return False


def resolve(c1, c2):
    temp = c1.union(c2)
    return [temp.difference({c, complement(c)}) for c in temp if '~' + c in temp]
