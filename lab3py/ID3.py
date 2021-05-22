from node import *
from util import *


class ID3:
    hyperparameters: list
    tree: Node

    def __init__(self, hyperparameters=None):
        self.hyperparameters = hyperparameters

    def fit(self, train_dataset, features, label):
        self.tree = self.__id3_build(train_dataset, train_dataset, features, label, self.hyperparameters)

    def predict(self, test_dataset):
        return [self.__predict_one(test) for test in test_dataset]

    def __id3_build(self, dataset, dataset_parent, features: set, label: str, depth_limit: int, depth=1):
        if not has_features(dataset):
            max_label_value = get_most_frequent_label_value(dataset_parent, label)
            return Node(max_label_value, depth)

        max_label_value = get_most_frequent_label_value(dataset, label)

        if not features or num_distinct_label_values(dataset, label) <= 1 or depth_limit == 0:
            return Node(max_label_value, depth)

        discriminative_feature = get_most_discriminative_feature(dataset, features, label)
        node = Node(discriminative_feature, depth, max_label_value)

        partitioned_dataset = partition_set_by_feature_values(dataset, discriminative_feature)

        for f_v in get_feature_values(dataset, discriminative_feature):
            new_features = features - set((discriminative_feature,))
            child = self.__id3_build(partitioned_dataset[f_v], dataset, new_features, label, depth_limit-1, depth + 1)
            node.add_child(f_v, child)

        return node

    def __predict_one(self, test):
        current_node = self.tree
        while not current_node.is_leaf():
            test_feature_value = test[current_node.feature]
            if test_feature_value not in current_node.children.keys():
                return current_node.most_frequent_label_value
            else:
                current_node = current_node.children[test_feature_value]

        return current_node.feature  # this is value of a label for leaves


def calculate_accuracy(dataset: list, predictions: list, label: str):
    correct = 0
    for i in range(0, len(predictions)):
        if dataset[i][label] == predictions[i]:
            correct += 1

    return correct / len(predictions)


def get_confusion_matrix(dataset: list, predictions: list, label: str):
    label_values = set(predictions)
    for test in dataset:
        label_values.add(test[label])

    label_values = list(label_values)
    label_values.sort()

    label_index = dict()
    n = len(label_values)
    for i in range(0, n):
        label_index[label_values[i]] = i

    matrix = [[0] * n for i in range(n)]  # row -> true class, column -> predicted class

    for i in range(0, len(predictions)):
        true_class = dataset[i][label]
        predicted_class = predictions[i]

        matrix[label_index[true_class]][label_index[predicted_class]] += 1

    return matrix
