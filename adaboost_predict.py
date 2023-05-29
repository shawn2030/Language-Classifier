from train import Train
from stump import Stump
from adaboost import Adaboost
import pickle


def classify(sentence):
    # filename = sys.argv[1]
    with open('test.txt', 'w') as filewriter:
        filewriter.write(sentence)

    with open('adaboost.model', "rb") as f:
        adaboost_obj = pickle.load(f)

        # print(type(adaboost_obj.stump_list))
        stump_list = adaboost_obj.stump_list
        train_obj = Train('test.txt')
        df = train_obj.read_file()
        df = train_obj.if_nl_article(df)
        df = train_obj.if_nl_preposition(df)
        df = train_obj.if_nl_conjunction(df)
        df = train_obj.if_eng_article(df)
        df = train_obj.if_eng_common(df)
        df = train_obj.if_eng_preposition(df)
        df = train_obj.if_eng_conjunction(df)
        df['predictions'] = None

        i = 0
        for idx, row in df.iterrows():
            sum = 0

            for stump in stump_list:
                column_name = stump.column_name
                if df[column_name][idx] == True:
                    stump.value = True
                    sum += stump.create_stump()
                elif df[column_name][idx] == False:
                    stump.value = False
                    sum += stump.create_stump()

            i += 1
            if sum > 1:
                # print(i, 'en')
                return 'English'
            else:
                # print(i, 'nl')
                return 'Dutch'


if __name__ == "__main__":
    sentence = "continued African, conference apartheid the he of repression a 1951, and together the president a"
    print(classify(sentence))