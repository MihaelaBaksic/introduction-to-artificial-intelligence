def state_space_loader(path):
    lines = []
    with open(path) as f:
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

        next_states_list = list()
        for next_state in trans_string.split(' '):
            (state_n, cost) = tuple(next_state.split(','))
            next_states_list.append((state_n, int(cost)))

        next_states_list.sort(key=lambda s: s[0])  # order alphabetically

        transitions[state] = next_states_list

    return initial_state, transitions, goal_state


def heuristic_loader(path):
    return {line.strip()[:line.find(':')]: int(line.strip()[(line.find(' ')+1):]) for line in open(path, 'r')}



