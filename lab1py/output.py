

def search_output(alg, file_path, found, visited_no, total_cost, path):
    print("# " + alg + ' ' + file_path)
    print('[FOUND_SOLUTION]: ' + found)
    print('[STATES_VISITED]: ' + str(visited_no))
    print('[PATH_LENGTH]: ' + str(len(path)))
    print('[TOTAL_COST]: ' + "{:.1f}".format(total_cost))
    print('[PATH]: ' + ' => '.join(path))
