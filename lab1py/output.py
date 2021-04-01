import path_calc


def search_output(alg, file_path, found, visited_no, total_cost, goal_node):
    path = path_calc.get_path(goal_node)
    print("# " + alg + ' ' + file_path)
    print('[FOUND_SOLUTION]: ' + found)
    print('[STATES_VISITED]: ' + str(visited_no))
    print('[PATH_LENGTH]: ' + str(len(path)))
    print('[TOTAL_COST]: ' + "{:.1f}".format(total_cost))
    print('[PATH]: ' + ' => '.join(path))


def optimistic_output(evaluation, path):
    print('# HEURISTIC_OPTIMISTIC: {}'.format(path))
    optimistic = True
    for state in evaluation:
        (heuristic, oracle) = evaluation[state]
        if heuristic > oracle:
            optimistic = False
        print('[CONDITION]: [{}] h({}) <= h*: {:.1f} <= {:.1f}'.format(
              'OK' if heuristic <= oracle else 'ERR', state, heuristic, oracle))

    print('[CONCLUSION]: Heuristic is {}optimistic.'.format('' if optimistic else 'not '))


def consistent_output(evaluation, path, h):

    print('# HEURISTIC_CONSISTENT: {}'.format(path))
    consistent = True
    for e in evaluation:
        condition = (int(h[e[0]]) <= int(h[e[1]]) + int(e[2]))
        if not condition:
            consistent = False
        print('[CONDITION]: {} h({}) <= h({}) + c: {} <= {} + {}'.format(
            '[OK]' if condition else '[ERR]',
            e[0], e[1],
            h[e[0]], h[e[1]], e[2]
        ))
    print('[CONCLUSION]: Heuristic is {}consistent.'.format('' if consistent else 'not '))
