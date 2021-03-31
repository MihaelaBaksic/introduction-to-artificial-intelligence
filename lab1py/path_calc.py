def get_path(goal_node):
    path = []
    current_node = goal_node
    path.insert(0, current_node[1])

    while current_node[4] is not None:
        current_node = current_node[4]
        path.insert(0, current_node[1])

    return path

