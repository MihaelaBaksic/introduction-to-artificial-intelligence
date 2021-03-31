def state_space_loader(path):
    lines = []
    with open(path) as f:
        for line in f:
            if line.strip()[0] == '#':
                continue
            lines.append(line.strip())

    initial_state = lines[0]
    goal_states = lines[1].split(' ')

    transitions = dict()

    for line in lines[2:]:
        state = line[:line.find(':')]
        space_pos = line.find(' ')
        trans_string = line[(space_pos + 1):] if space_pos >= 0 else ''

        next_states_list = list()
        if trans_string != '':
            for next_state in trans_string.split(' '):
                (state_n, cost) = tuple(next_state.split(','))
                next_states_list.append((state_n, int(cost)))

        next_states_list.sort(key=lambda s: s[0])  # order alphabetically

        transitions[state] = next_states_list

    return initial_state, transitions, goal_states, transitions.keys()


def heuristic_loader(path):
    return {line.strip()[:line.find(':')]: int(line.strip()[(line.find(' ') + 1):]) for line in open(path, 'r')}
