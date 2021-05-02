from util import *


def resolution(premises: set, neg_goal: set):
    knowledge = remove_redundant(remove_irrelevant(premises))
    set_of_support = remove_redundant(remove_irrelevant(neg_goal))

    checked = set()

    parents = dict()

    while True:
        new = set()
        # print(knowledge)
        for c1, c2 in select_clauses(set_of_support, knowledge):

            if (c1, c2) in checked or (c2, c1) in checked:
                continue
            checked.add((c1, c2))

            res = remove_irrelevant(resolve(c1, c2))

            for r in res:
                parents[to_string(r)] = (to_string(c1), to_string(c2))

            # print(str(c1) + ' + ' + str(c2) + ' = ' + str(res))
            if set() in res:
                return True, parents

            new = new.union(res)

        if all(r in knowledge.union(set_of_support) for r in new):
            return False, parents

        knowledge = remove_redundant(remove_irrelevant(knowledge.union(set_of_support)))
        set_of_support = remove_redundant(remove_irrelevant(new))


def select_clauses(sos, knowledge):
    # at least one in the pair should come from set of support
    selected_clauses = []

    second = sos.union(knowledge)

    for clause1 in sos:
        for clause2 in second:
            if can_be_resolved(clause1, clause2) and (clause2, clause1) not in selected_clauses:
                selected_clauses.append((clause1, clause2))

    return selected_clauses


def resolve(c1, c2):
    temp = c1.union(c2)
    return [frozenset(temp.difference({c, complement(c)})) for c in temp if '~' + c in temp]
