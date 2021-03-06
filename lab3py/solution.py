import arguments
import loader
from ID3 import *

if __name__ == '__main__':

    training_set, label, features = loader.load_training_dataset(arguments.args.training)

    test_set = loader.load_test_dataset(arguments.args.test)

    depth_limit = math.inf
    if arguments.args.depth is not None:
        depth_limit = int(arguments.args.depth)

    model = ID3(depth_limit)
    model.fit(training_set, features, label)
    print("[BRANCHES]:")
    for branch in tree_branches(model.tree):
        print(branch)

    predictions = model.predict(test_set)
    print("[PREDICTIONS]: " + " ".join(predictions))

    accuracy = calculate_accuracy(test_set, predictions, label)
    print("[ACCURACY]: {0:.5f}".format(round(accuracy, 5)))

    print("[CONFUSION_MATRIX]:")
    matrix = get_confusion_matrix(test_set, predictions, label)

    for line in matrix:
        print(" ".join([str(x) for x in line]))


