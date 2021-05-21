from node import *
from util import *
class ID3:

    hyperparameters: list
    tree: Node

    def __init__(self, hyperparameters=None):
        self.hyperparameters = hyperparameters

    def fit(self, train_dataset, features, label):
        self.tree = id3_build(train_dataset, train_dataset, features, label)

    def predict(self, test_dataset):
        return test_dataset


def id3_build(dataset, dataset_parent, features: set, label: str):
    if not has_features(dataset):
        max_label_value = get_most_frequent_label_value(dataset_parent, label)
        return Node(max_label_value)

    max_label_value = get_most_frequent_label_value(dataset, label)
    max_label_dataset = get_partition_for_label_value(dataset, label, max_label_value)
    if not features or dataset_equals(dataset, max_label_dataset):
        return Node(max_label_value)

    discriminative_feature = get_most_discriminative_feature(dataset, features, label)
    node = Node(discriminative_feature)
    partitioned_dataset = partition_set_by_feature_values(dataset, discriminative_feature)

    for f_v in get_feature_values(dataset, discriminative_feature):
        child = id3_build(partitioned_dataset[f_v], dataset, features - discriminative_feature, label)
        node.add_child(f_v, child)

    return node

