
class ID3:

    hyperparameters: list

    def __init__(self, hyperparameters=None):
        self.hyperparameters = hyperparameters

    def fit(self, train_dataset):
        return train_dataset

    def predict(self, test_dataset):
        return test_dataset
