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

def consistent_output():
    a = 0
