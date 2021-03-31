def get_path(goal_node):
    path = []
    current_node = goal_node
    path.insert(0, current_node[0])

    while current_node[3] is not None:
        current_node = current_node[3][1:]
        path.insert(0, current_node[0])

    return path

