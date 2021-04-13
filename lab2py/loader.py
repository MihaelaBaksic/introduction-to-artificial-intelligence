def load_clauses(path: str):
    clauses = []
    with open(path) as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            clauses.append({x.strip().lower() for x in line.split('v')})

    return clauses[-1:], clauses[0:-1]



