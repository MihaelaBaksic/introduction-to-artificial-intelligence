class Node:
    feature: str
    children: dict  # key is feature_value, value is next Node
    depth: int
    most_frequent_label_value: str

    def __init__(self, feature: str, depth: int, most_freq=None):
        self.feature = feature
        self.children = dict()
        self.depth = depth
        if most_freq is None:  # for leaves
            self.most_frequent_label_value = feature
        else:  # for nodes
            self.most_frequent_label_value = most_freq

    def add_child(self, feature_value, child):
        assert feature_value not in self.children.keys()
        self.children[feature_value] = child

    def is_leaf(self):
        return not bool(self.children)


def tree_branches(node, previous):
    branches = list()

    if node.is_leaf():
        s = previous + " " + node.feature
        branches.append(s)
        return branches

    previous += " " + node.depth + ":"
