from train import Train
from stump import Stump
import pandas as pd
import math
import random
import pickle


class Adaboost:
    def __init__(self):
        self.stump_list = self.adaboost()

    def adaboost(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        train_obj = Train('dataset.txt')
        stump_list = []

        df = train_obj.read_file()
        df = train_obj.if_nl_article(df)
        df = train_obj.if_nl_preposition(df)
        df = train_obj.if_nl_conjunction(df)
        df = train_obj.if_eng_article(df)
        df = train_obj.if_eng_common(df)
        df = train_obj.if_eng_preposition(df)
        df = train_obj.if_eng_conjunction(df)

        df['weights'] = None
        df['updated_weight'] = None
        df['normalized_weight'] = None


        #######       updated the weights column in df  for 1st iteration
        for idx, row in df.iterrows():
            df['weights'][idx] = ( 1 /  df.shape[0] )

        # print(df['weights'])

        for i in range(100):
            df['max_window'] = None
            df['min_window'] = None

            #######      calculate entropy
            columns = ['if_eng_conjunction', 'if_eng_preposition', 'if_eng_article', 'if_nl_article',
                           'if_nl_conjunction', 'if_nl_preposition', 'if_eng_common']

            entropy_list = []

            for column in columns:
                remainder, _, _ = train_obj.test_column_remainder(df, column)
                entropy_list.append(remainder)

            min_entropy = min(entropy_list)
            column_name = columns[entropy_list.index(min_entropy)]
            print(column_name)


            total_error, incorrect_index = self.calculate_error(df, column_name)
            print("total error = " + str(total_error))

            if total_error == 0:
                break
            alpha = self.calculate_alpha(total_error)

            df = self.update_truly_classified_weights(df, incorrect_index, alpha)
            df = self.update_falsely_classified_weights(df, incorrect_index, alpha)


            print("#########  creating a stump and adding the stump to a list")
            stump_obj = Stump(column_name = column_name, alpha= alpha)
            stump_list.append(stump_obj)


            print("####### got the normalized weights")
            df = self.normalize_weights(df)



            print("#######  creating a new dataset")
            df = self.create_updated_dataset(df)
            # print(df)
            print(stump_obj.column_name)
            print(stump_obj.alpha)

        print(stump_list)

        return stump_list

    def create_updated_dataset(self,df):
        new_df = df

        new_new_df = pd.DataFrame(columns = new_df.columns)

        #######     fill the window

        accumulate_normalized_weight = new_df['normalized_weight'][1]
        new_df['max_window'][0] = new_df['normalized_weight'][1]
        new_df['min_window'][0] = 0
        for index in range(1, df.shape[0]):
            min_range = accumulate_normalized_weight
            new_df['min_window'][index] = min_range
            accumulate_normalized_weight += new_df['normalized_weight'][index]
            max_range = accumulate_normalized_weight
            new_df['max_window'][index] = max_range

        # print(new_df['min_window'], new_df['max_window'])

        # print(new_df.columns)
        # print(new_new_df.columns)


        for i, df_row in df.iterrows():
            random_number = round(random.random(), 6)
            for idx, new_df_row in new_df.iterrows():
                if random_number < new_df['max_window'][idx] and random_number >= new_df['min_window'][idx]:
                    new_new_df.loc[i] = new_df.loc[idx]

        # print(new_new_df)

        new_new_df = new_new_df.reset_index(drop = True)

        return new_new_df


    def normalize_weights(self, df):
        total_updated_weight = 0
        for index, rows in df.iterrows():
            total_updated_weight += df['updated_weight'][index]

        for index, rows in df.iterrows():
            normalized_weight = float( df['updated_weight'][index] / total_updated_weight )
            df['normalized_weight'][index] = normalized_weight

        return df

    def update_truly_classified_weights(self,df, incorrect_index, alpha):
        for index, rows in df.iterrows():
            if index not in incorrect_index:
                weight = df['weights'][index]
                df['updated_weight'][index] = weight * math.exp((-1)*alpha)

        return df


    def update_falsely_classified_weights(self, df, incorrect_index, alpha):
        for index in incorrect_index:
            weight = df['weights'][index]
            df['updated_weight'][index] = weight * math.exp(alpha)

        return df


    def calculate_alpha(self,total_error):
        alpha = 0.5 * math.log(float(1 - total_error) / total_error)
        return alpha


    def calculate_error(self,df, column_name):
        eng = []
        eng_idx = []
        dutch = []
        dutch_idx = []
        for i, row in df.iterrows():
            if column_name == 'if_nl_article':
                if df[column_name][i] == True:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue

            if column_name == 'if_nl_preposition':
                if df[column_name][i] == True:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue

            if column_name == 'if_nl_conjunction':
                if df[column_name][i] == True:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue

            if column_name == 'if_eng_article':
                if df[column_name][i] == True:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue

            if column_name == 'if_eng_common':
                if df[column_name][i] == True:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue

            if column_name == 'if_eng_preposition':
                if df[column_name][i] == True:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue

            if column_name == 'if_eng_conjunction':
                if df[column_name][i] == True:
                    eng.append(df['language'][i])
                    eng_idx.append(i)
                    continue
                elif df[column_name][i] == False:
                    dutch.append(df['language'][i])
                    dutch_idx.append(i)
                    continue



        errors = 0
        incorrect_index = []
        # print(eng)
        # print(eng_idx)
        # print(dutch)
        #
        # print(dutch_idx)
        for i in range(len(eng)):
            if eng[i] == 'nl':
                errors += df['weights'][eng_idx[i]]
                incorrect_index.append(eng_idx[i])

        for i in range(len(dutch)):
            if dutch[i] == 'en':
                errors += df['weights'][dutch_idx[i]]
                incorrect_index.append(dutch_idx[i])

        return errors, incorrect_index


if __name__ == "__main__":
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    stump_list = Adaboost()
    with open('adaboost.model', 'wb') as adaboost_writer:
        pickle.dump(stump_list, adaboost_writer)




