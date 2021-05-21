import math


def entropy(dataset: list, label: str):
    label_values = list(map(lambda x: x[label], dataset))
    label_set = set(label_values)

    E = 0.
    num_examples = len(label_values)

    for l in label_set:
        probability = label_values.count(l) / num_examples
        E -= probability * math.log2(probability)

    assert 0 <= E <= math.log2(len(label_set))
    return E


def information_gain(dataset: list, label: str, feature: str):
    E = entropy(dataset, label)
    partition_set_by_feature_values(dataset, feature)

    IG = E
    partitions = partition_set_by_feature_values(dataset, feature)
    for partition in partitions.values():
        E_p = entropy(partition, label)
        IG -= len(partition) * E_p / len(dataset)

    return IG


def partition_set_by_feature_values(dataset: list, feature: str):
    partitions = dict()

    for entry in dataset:
        feature_value = entry[feature]
        if feature_value not in partitions.keys():
            partitions[entry[feature]] = list()

        par_entry = entry.copy()
        del par_entry[feature]
        partitions[feature_value].append(par_entry)

    print(partitions)
    return partitions
