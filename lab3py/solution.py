import arguments
import loader
import util
from ID3 import *

if __name__ == '__main__':

    training_set, label, features = loader.load_training_dataset(arguments.args.training)
    # print("IG A: " + str(util.information_gain(training_set, label, 'temperature')))

    model = ID3()
    model.fit(training_set, features, label)
