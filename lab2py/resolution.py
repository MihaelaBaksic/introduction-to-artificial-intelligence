def resolution(clauses: set, goal_clause):
    new = set()
    resolved_pairs = set()

    while True:
        for (c1, c2) in select_clauses(clauses):
            if (c1, c2) in resolved_pairs or (c2, c1) in resolved_pairs:
                continue

            resolved_pairs.add((c1, c2))
            resolvents = resolve(c1, c2)
            if 'NIL' in resolvents:
                return True
            new.add(resolvents)

        if new < clauses:  # subset or real subset ??
            return False

        clauses.add(new)


def select_clauses(clauses):  # 1 or 2 should come from neg_goal + newly_derived, fix it in the main alg as well
    return 1  # TODO


def resolve(c1, c2):
    return 1  # TODO
