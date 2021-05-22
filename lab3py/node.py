import queue


class Node:
    feature: str
    children: dict  # key is feature_value, value is next Node
    depth: int
    most_frequent_label_value: str
    parent: None
    path_from_parent: str

    def __init__(self, feature: str, depth: int, most_freq=None):
        self.feature = feature
        self.children = dict()
        self.depth = depth
        self.parent = None
        self.path_from_parent = None
        if most_freq is None:  # for leaves
            self.most_frequent_label_value = feature
        else:  # for nodes
            self.most_frequent_label_value = most_freq

    def add_child(self, feature_value, child):
        assert feature_value not in self.children.keys()
        self.children[feature_value] = child
        child.parent = self
        child.path_from_parent = feature_value

    def is_leaf(self):
        return not bool(self.children)


def tree_branches(node):
    leafs = queue.Queue()
    to_check = queue.Queue()

    to_check.put(node)

    while not to_check.empty():
        current_node = to_check.get()
        if current_node.is_leaf():
            leafs.put(current_node)
        else:
            for child in current_node.children.values():
                to_check.put(child)

    branches = []

    while not leafs.empty():
        branches.append(leaf_track(leafs.get()))

    return branches


def leaf_track(leaf):
    s = leaf.feature  # leaf value

    node = leaf.parent
    feature_value = leaf.path_from_parent
    while node is not None:
        n = str(node.depth) + ':' + node.feature + '=' + feature_value
        s = n + ' ' + s
        feature_value = node.path_from_parent
        node = node.parent

    return s
