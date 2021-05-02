def complement(c):
    return '~' + c if c[0] != '~' else c[1:]


def remove_irrelevant(clauses: set):
    return {clause for clause in clauses if not is_tautology(clause)}


def remove_redundant(clauses: set, complete_knowledge: set):
    return {c1 for c1 in clauses if not any(c1 >= c2 and c1 != c2 for c2 in complete_knowledge)}


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
        for child, parents in resolution.items():
            if parents[0] not in resolution and parents[0] not in premises:
                premises.append(parents[0])
            if parents[1] not in resolution and parents[1] not in premises:
                premises.append(parents[1])

            resolvents.insert(0, (child, parents[0], parents[1]))

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


def print_knowledge(clauses: set):
    print('Constructed with knowledge:')
    cnt = 1
    for c in clauses:
        print(str(cnt) + '. ' + to_string(c))
    print('===============')
