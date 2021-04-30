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
    for literal in clause:
        if complement(literal) in clause:
            return True
    return False


def can_be_resolved(c1, c2):
    for a1 in c1:
        if complement(a1) in c2:
            return True

    return False


def is_subset(l1, l2):
    for elem in l1:
        if elem not in l2:
            return False

    return True


def print_results(resolution: dict):
    premises = []
    resolvents = []

    res_queue = []

    try:
        nil_parents = resolution['NIL']
        resolvents.insert(0, ('NIL', *nil_parents))

        res_queue.append(nil_parents[0])
        res_queue.append(nil_parents[1])

        while len(res_queue) != 0:
            r = res_queue.pop()
            try:
                parents = resolution[r]
                resolvents.insert(0, (r, *parents))
                res_queue.append(parents[0])
                res_queue.append(parents[1])
            except KeyError:
                premises.append(r)

    except KeyError:
        return

    resolvents = [(r[0], get_index(r[1], premises, resolvents), get_index(r[2], premises, resolvents)) for r in
                  resolvents]
    resolvents = sorted(resolvents, key=lambda x: max(x[1], x[2]))

    cnt = 1
    for p in premises:
        print(str(cnt) + '. ' + p)
        cnt += 1
    print("===============")
    for r in resolvents:
        print(str(cnt) + '. ' + r[0] + ' (' + str(r[1]) + ', ' + str(r[2]) + ')')
        cnt += 1
    print("===============")


def to_string(clause: frozenset):
    if clause == frozenset():
        return 'NIL'

    s = ''
    for literal in clause:
        s += literal + ' v '
    return s[:-3]


def get_index(clause, premises, resolvents):
    prem_len = len(premises)
    for i in range(0, prem_len):
        if premises[i] == clause:
            return i + 1

    for i in range(0, len(resolvents)):
        if resolvents[i][0] == clause:
            return prem_len + i + 1

    return -1
