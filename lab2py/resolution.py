from util import *


def resolution(premises: list, set_of_support: list):
    new = list()
    resolved_pairs = list()

    while True:
        new = list()
        for c1, c2 in select_clauses(premises, set_of_support):
            if (c1, c2) in resolved_pairs or (c2, c1) in resolved_pairs:
                continue

            print("Resolving" + str(c1) + ' ' + str(c2))

            resolved_pairs.append((c1, c2))
            resolvents = resolve(c1, c2)

            if set() in resolvents:
                return True

            new.extend(remove_irrelevant(resolvents))

        if is_subset(new, set_of_support):  # subset or real subset ??
            return False

        set_of_support.extend(new)
        print("SoS: " + str(set_of_support))
        # set_of_support = remove_redundant(set_of_support)
        print("SoS: " + str(set_of_support))


#  add removal of redundant and irrelevant clauses


def select_clauses(premises, set_of_support):
    # at least one in the pair should come from set of support
    selected_clauses = []

    for c1 in set_of_support:
        for c2 in premises + set_of_support:
            if can_be_resolved(c1, c2) and (c2, c1) not in selected_clauses:  # not in selected_clauses can maybe be removed ??
                selected_clauses.append((c1, c2))

    return selected_clauses


def can_be_resolved(c1, c2):
    for a1 in c1:
        if complement(a1) in c2:
            return True

    return False


def resolve(c1, c2):
    temp = c1.union(c2)
    return [temp.difference({c, complement(c)}) for c in temp if '~'+c in temp]



