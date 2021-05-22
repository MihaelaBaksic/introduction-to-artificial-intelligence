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

    return partitions


def get_partition_for_feature_value(dataset: list, feature: str, feature_value: str):
    partitions = partition_set_by_feature_values(dataset, feature)

    if feature_value in partitions:
        return partitions[feature_value]
    else:
        # do something defined in the PDF
        return 1


def has_features(dataset):
    for example in dataset:
        if len(example.keys()) <= 1:
            return False
    return True


def get_partition_for_label_value(dataset, label, label_value):
    return [e for e in dataset if e[label] == label_value]


def get_most_frequent_label_value(dataset, label):
    label_frequencies = dict()

    for example in dataset:
        label_value = example[label]
        if label_value not in label_frequencies.keys():
            label_frequencies[label_value] = 0
        label_frequencies[label_value] += 1

    return max(label_frequencies.keys(), key=lambda l: (label_frequencies[l], l))


def dataset_equals(ds1, ds2):
    return False


def num_distinct_label_values(dataset: list, label:str):
    values = set()
    for example in dataset:
        values.add(example[label])

    return len(values)


def get_most_discriminative_feature(dataset: list, features: set, label: str):
    return max(features, key=lambda f: (information_gain(dataset, label, f), f))


def get_feature_values(dataset, feature):
    return {f[feature] for f in dataset if feature in f.keys()}


