class Node:
    feature: str
    children: dict  # key is feature_value, value is next Node

    def __init__(self, feature: str):
        self.feature = feature
        self.children = dict()

    def add_child(self, feature_value, child):
        assert feature_value not in self.children.keys()
        self.children[feature_value] = child

    def is_leaf(self):
        return not bool(self.children)

