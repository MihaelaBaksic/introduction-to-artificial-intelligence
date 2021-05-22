import csv


def load_training_dataset(path: str):
    dataset = []

    with open(path) as f:
        reader = csv.reader(f, delimiter=',')
        features = next(reader)

        label = features[-1]

        for row in reader:
            data_row = dict()
            for value_idx in range(0, len(row)):
                data_row[features[value_idx]] = row[value_idx]
            dataset.append(data_row)

    return dataset, label, set(features[0:-1])


def load_test_dataset(path: str):
    dataset = []

    with open(path) as f:
        reader = csv.reader(f, delimiter=',')
        features = next(reader)

        for row in reader:
            data_row = dict()
            for value_idx in range(0, len(row)):
                data_row[features[value_idx]] = row[value_idx]
            dataset.append(data_row)

    return dataset


