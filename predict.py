import pickle
from train import Train

import sys

# script, dt_model, filename = sys.argv

def classify(sentence):
    # filename = sys.argv[1]
    with open('test.txt', 'w') as filewriter:
        filewriter.write(sentence)

    with open('best.model', "rb") as f:
        # load the pickled object
        train_class = pickle.load(f)

        train = train_class('test.txt')
        df = train.test_tree()
        for i,rows in df.iterrows():
            # print(rows['prediction'])
            return rows['prediction']

if __name__ == "__main__":
    classify()



# train_obj = train_class('test.txt')

# train_obj.tree()