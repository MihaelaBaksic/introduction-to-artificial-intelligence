import util


def resolution(clauses: list, goal_clause: str):
    new = set()
    resolved_pairs = set()

    while True:
        for (c1, c2) in select_clauses(clauses):
            if (c1, c2) in resolved_pairs or (c2, c1) in resolved_pairs:
                continue

            resolved_pairs.add((c1, c2))
            resolvents = resolve(c1, c2)
            if set() in resolvents:
                return True
            new.add(resolvents)

        if new < clauses:  # subset or real subset ??
            return False

        clauses.add(new)
#  add removal of redundant and irrelevant clauses


def select_clauses(clauses):
    # 1 or 2 should come from neg_goal + newly_derived (set of support) , fix it in the main alg as well
    return 1  # TODO


def resolve(c1, c2):
    temp = c1.union(c2)
    return [temp.difference({c, complement(c)}) for c in temp if complement(c) in temp]


def complement(c):
    return '~' + c
