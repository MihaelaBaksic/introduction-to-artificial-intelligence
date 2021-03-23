def state_space_loader():
    lines = []
    with open('input.in') as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            lines.append(line.strip())

    initial_state = lines[0]
    goal_state = lines[1]

    transitions = dict()

    for line in lines[2:]:
        state = line[:line.find(':')]
        trans_string = line[(line.find(' ')+1):]

        next_states_set = set()
        for next_state in trans_string.split(' '):
            (state, cost) = tuple(next_state.split(','))
            next_states_set.add((state, int(cost)))

        transitions[state] = next_states_set

    return initial_state, goal_state, transitions


def heuristic_loader():
    return [(line.strip()[:line.find(':')], int(line.strip()[(line.find(' ')+1):])) for line in open('heuristic.in', 'r')]



