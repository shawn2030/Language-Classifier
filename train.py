import pandas as pd
import math
import pickle


class Train:

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        # df = pd.read_csv('dataset.txt', delimiter='|', header=None)
        with open(self.filename, 'r') as f:
            line = f.readlines()
            first_line = line[0]
            if '|' in first_line:
                df = pd.read_csv(self.filename, delimiter='|', header=None)

                df.columns = ['language', 'sentence']
            else:
                df = pd.DataFrame({'sentence': line})

        return df

    def if_eng_article(self,df):
        df_article = df
        df_article['if_eng_article'] = None
        for i, line in enumerate(df_article['sentence']):
            line = line.lower()
            line = line.split()
            if 'a' in line or 'an' in line or 'the' in line:
                df_article['if_eng_article'][i] = True
            else:
                df_article['if_eng_article'][i] = False

        return df_article


    def if_eng_preposition(self,df):
        df_prepos = df
        df_prepos['if_eng_preposition'] = None
        prepositions = ['about', 'above', 'across', 'after', 'against', 'along', 'amid', 'amidst', 'among', 'amongst',
                        'around', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond',
                        'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'for', 'from', 'in',
                        'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past',
                        'regarding', 'round', 'since', 'through', 'throughout', 'to', 'toward', 'towards', 'under',
                        'underneath', 'until', 'till', 'up', 'upon', 'with', 'within', 'without']

        for i, line in enumerate(df_prepos['sentence']):
            line = line.lower()
            line = line.split()
            # if 'a' in line or 'an' in line or 'the' in line:
            #     df_prepos['if_eng_prepos'][i] = True
            # else:
            #     df_prepos['if_eng_prepos'][i] = False
            for word in line:
                if word in prepositions:
                    df_prepos['if_eng_preposition'][i] = True
                # else:
                #     df_prepos['if_eng_prepos'][i] = False
            if df_prepos['if_eng_preposition'][i] != True:
                df_prepos['if_eng_preposition'][i] = False


        return df_prepos

    def if_eng_common(self,df):
        df_common = df
        df_common['if_eng_common'] = None
        common = ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
                        'this', 'that', 'these', 'those', 'here', 'there', 'now', 'then', 'always', 'never',
                        'sometimes', 'often', 'rarely', 'quickly', 'slowly', 'easily', 'hard', 'well', 'better',
                        'best', 'worse', 'worst', 'more', 'most', 'least', 'all', 'some', 'none', 'many', 'few',
                        'every', 'any', 'such', 'no', 'other', 'another', 'enough', 'even',
                        'always', 'never', 'sometimes', 'often', 'rarely', 'quickly', 'slowly', 'easily', 'hard', 'well', 'better', 'best',
                         'worse', 'worst', 'more', 'most', 'least', 'all', 'some', 'none', 'many']

        for i, line in enumerate(df_common['sentence']):
            line = line.lower()
            line = line.split()
            # if 'a' in line or 'an' in line or 'the' in line:
            #     df_prepos['if_eng_prepos'][i] = True
            # else:
            #     df_prepos['if_eng_prepos'][i] = False
            for word in line:
                if word in common:
                    df_common['if_eng_common'][i] = True
                # else:
                #     df_prepos['if_eng_prepos'][i] = False
            if df_common['if_eng_common'][i] != True:
                df_common['if_eng_common'][i] = False


        return df_common


    def if_eng_conjunction(self,df):
        df_conj = df
        df_conj['if_eng_conjunction'] = None
        conjunctions = ['and', 'or', 'but', 'so', 'for', 'yet', 'nor', 'although', 'because', 'since', 'unless', 'while',
                        'whereas', 'if']

        for i, line in enumerate(df_conj['sentence']):
            line = line.lower()
            line = line.split()
            # if 'is' in line:
            #     df_is['if_is'][i] = True
            # else:
            #     df_is['if_is'][i] = False
            for word in line:
                if word in conjunctions:
                    df_conj['if_eng_conjunction'][i] = True
            if df_conj['if_eng_conjunction'][i] != True:
                df_conj['if_eng_conjunction'][i] = False

        return df_conj


    def if_nl_article(self,df):
        df_article = df
        df_article['if_nl_article'] = None
        for i, line in enumerate(df_article['sentence']):
            line = line.lower()
            line = line.split()
            if 'de' in line or 'het' in line or 'een' in line:
                df_article['if_nl_article'][i] = True
            else:
                df_article['if_nl_article'][i] = False

        return df_article

    def if_nl_preposition(self,df):
        prepositions = ['aan', 'achter', 'bij', 'binnen', 'buiten', 'door', 'in', 'langs', 'met', 'na', 'naar', 'onder',
                        'op', 'over', 'tegen', 'tussen', 'uit', 'van', 'voor', 'onder', 'langs', 'rond', 'om', 'tot']
        df_prepos = df
        df_prepos['if_nl_preposition'] = None

        for i, line in enumerate(df_prepos['sentence']):
            line = line.lower()
            line = line.split()
            for word in line:
                if word in prepositions:
                    df_prepos['if_nl_preposition'][i] = True
                # else:
                #     df_prepos['if_eng_prepos'][i] = False
            if df_prepos['if_nl_preposition'][i] != True:
                df_prepos['if_nl_preposition'][i] = False

        return df_prepos

    def if_nl_conjunction(self,df):
        conjunctions = ['en', 'of', 'maar', 'dus', 'ofwel', 'noch', 'hoewel', 'omdat', 'sinds', 'tenzij', 'terwijl',
                        'waar', 'indien', 'zodra', 'eerder', 'dan', 'alsof', 'alsook']

        df_conj = df
        df_conj['if_nl_conjunction'] = None

        for i, line in enumerate(df_conj['sentence']):
            line = line.lower()
            line = line.split()
            # if 'is' in line:
            #     df_is['if_is'][i] = True
            # else:
            #     df_is['if_is'][i] = False
            for word in line:
                if word in conjunctions:
                    df_conj['if_nl_conjunction'][i] = True
            if df_conj['if_nl_conjunction'][i] != True:
                df_conj['if_nl_conjunction'][i] = False

        return df_conj


    def test_column_remainder(self,df, column_name):
        level1_True = []
        level1_False = []
        parent_node_length = df.shape[0]
        # print(parent_node_length)
        df_True_index = []
        df_False_index = []
        for i in range(df.shape[0]):
            if df[column_name][i] == True:
                level1_True.append(df['language'][i])
                df_True_index.append(i)
            elif df[column_name][i] == False:
                level1_False.append(df['language'][i])
                df_False_index.append(i)

        remainder = self.remainder_formula(level1_True, level1_False, parent_node_length)

        return remainder, df_True_index, df_False_index

    def true_false_indices(self, df, column_name):
        df_True_index = []
        df_False_index = []
        for i in range(df.shape[0]):
            if df[column_name][i] == True:
                df_True_index.append(i)
            elif df[column_name][i] == False:
                df_False_index.append(i)


        return  df_True_index, df_False_index


    def remainder_formula(self,True_list: list, False_list: list, parent_node_length: int):

        length_true = len(True_list)
        length_false = len(False_list)

        num_en_true = []
        num_nl_true = []
        num_en_false = []
        num_nl_false = []

        for i in True_list:
            if i == 'en':
                num_en_true.append(i)
            elif i == 'nl':
                num_nl_true.append(i)

        for i in False_list:
            if i == 'en':
                num_en_false.append(i)
            elif i == 'nl':
                num_nl_false.append(i)

        if  parent_node_length == 0 or length_true == 0 or len(num_en_true) == 0 or len(num_nl_true)  == 0:
            true_remainder = 0

        else:
            true_remainder = (length_true / parent_node_length) * (
                    (len(num_en_true) / length_true) * math.log2(1 / (len(num_en_true) / length_true)) + (
                    (len(num_nl_true) / length_true) * (math.log2(1 / (len(num_nl_true) / length_true)))))

        if  parent_node_length == 0 or length_false == 0 or len(num_en_false) == 0 or len(num_nl_false) == 0:
            false_remainder = 0


        else:
            false_remainder = (length_false / parent_node_length) * (
                    (len(num_en_false) / length_false) * math.log2(1 / (len(num_en_false) / length_false)) + (
                    (len(num_nl_false) / length_false) * (math.log2(1 / (len(num_nl_false) / length_false)))))

        return (true_remainder + false_remainder / 2)


    def train_tree(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        df = self.read_file()
        df = self.if_eng_article(df)
        df = self.if_eng_conjunction(df)
        df = self.if_eng_preposition(df)
        df  = self.if_nl_article(df)
        df = self.if_nl_conjunction(df)
        df = self.if_nl_preposition(df)
        df = self.if_eng_common(df)
        df['prediction'] = None


    ###################         level 2         ##########################
        columns_level1 = ['if_eng_conjunction', 'if_eng_preposition', 'if_eng_article', 'if_nl_article',
                   'if_nl_conjunction', 'if_nl_preposition', 'if_eng_common']
        for column_name in columns_level1:
            remainder, _, _ = self.test_column_remainder(df, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df, 'if_nl_article')

        df_True_level2 = pd.DataFrame(columns=df.columns)
        df_False_level2 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df.loc[idx]
            df_True_level2 = df_True_level2._append(row)

        for idx in false_index:
            row = df.loc[idx]
            df_False_level2 = df_False_level2._append(row)

        df_True_level2 = df_True_level2.reset_index(drop = True)
        df_False_level2 = df_False_level2.reset_index(drop = True)

        # print(df_True_level2.shape[0])
        # print(df_False_level2)


    ###################         level 2   TRUE      ##########################


        columns_level2 = [ 'if_eng_conjunction', 'if_eng_preposition', 'if_eng_article','if_nl_conjunction', 'if_nl_preposition']

        for column_name in columns_level2:
            remainder, _, _ = self.test_column_remainder(df_True_level2, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_True_level2, 'if_nl_preposition')

        df_True_level3 = pd.DataFrame(columns=df.columns)
        df_False_level3 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_True_level2.loc[idx]
            df_True_level3 = df_True_level3._append(row)

        for idx in false_index:
            row = df_False_level2.loc[idx]
            df_False_level3 = df_False_level3._append(row)

        df_True_level3 = df_True_level3.reset_index(drop=True)
        df_False_level3 = df_False_level3.reset_index(drop=True)

        # print(df_True_level3)
        # print(df_False_level3)
    ###################         level 3   TRUE -> TRUE      ##########################

        for index, row in df_True_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'

    ###################         level 3   TRUE -> FALSE     ##########################

        for index, row in df_False_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

    #############################################################################

    ###################         level 2   False     ##########################

        columns_level2 = [ 'if_eng_conjunction', 'if_eng_preposition', 'if_eng_article','if_nl_conjunction', 'if_nl_preposition', 'if_eng_common']

        for column_name in columns_level2:
            remainder, _, _ = self.test_column_remainder(df_False_level2, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_False_level2, 'if_eng_article')
        #
        df_False_True_level3 = pd.DataFrame(columns=df.columns)
        df_False_False_level3 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_level2.loc[idx]
            df_False_True_level3 = df_False_True_level3._append(row)

        for idx in false_index:
            row = df_False_level2.loc[idx]
            df_False_False_level3 = df_False_False_level3._append(row)

        df_False_True_level3 = df_False_True_level3.reset_index(drop=True)
        df_False_False_level3 = df_False_False_level3.reset_index(drop=True)

        # print(df_False_True_level3)
        # print(df_False_False_level3)


    ###################         level 3   FALSE -> TRUE    ##########################

        for index, row in df_False_True_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

    ###################         level 3   FALSE -> FALSE    ##########################

        columns_level3 = [ 'if_eng_conjunction', 'if_eng_preposition', 'if_nl_conjunction', 'if_nl_preposition', 'if_eng_common']

        for column_name in columns_level3:
            remainder, _, _ = self.test_column_remainder(df_False_False_level3, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_False_False_level3, 'if_eng_conjunction')
        #
        df_False_False_True_level4 = pd.DataFrame(columns=df.columns)
        df_False_False_False_level4 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_level3.loc[idx]
            df_False_False_True_level4 = df_False_False_True_level4._append(row)

        for idx in false_index:
            row = df_False_False_level3.loc[idx]
            df_False_False_False_level4 = df_False_False_False_level4._append(row)

        df_False_False_True_level4 = df_False_False_True_level4.reset_index(drop=True)
        df_False_False_False_level4 = df_False_False_False_level4.reset_index(drop=True)

        # print(df_False_False_True_level4)
        # print(df_False_False_False_level4)

    ###################         level 3   FALSE -> FALSE -> TRUE   ##########################

        for index, row in df_False_False_True_level4.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

    ###################         level 3   FALSE -> FALSE -> FALSE   ##########################

        columns_level4 = [ 'if_eng_preposition', 'if_nl_conjunction', 'if_nl_preposition', 'if_eng_common']

        for column_name in columns_level4:
            remainder, _, _ = self.test_column_remainder(df_False_False_False_level4, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_False_False_False_level4, 'if_eng_common')

        df_False_False_False_True_level5 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_level5 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_level4.loc[idx]
            df_False_False_False_True_level5 = df_False_False_False_True_level5._append(row)

        for idx in false_index:
            row = df_False_False_False_level4.loc[idx]
            df_False_False_False_False_level5 = df_False_False_False_False_level5._append(row)

        df_False_False_False_True_level5 = df_False_False_False_True_level5.reset_index(drop=True)
        df_False_False_False_False_level5 = df_False_False_False_False_level5.reset_index(drop=True)

        # print(df_False_False_False_True_level5)
        # print(df_False_False_False_False_level5)


    ###################         level 4   FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_True_level5.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

    ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE  ##########################

        columns_level5 = [ 'if_eng_preposition', 'if_nl_conjunction', 'if_nl_preposition']

        for column_name in columns_level5:
            remainder, _, _ = self.test_column_remainder(df_False_False_False_False_level5, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_False_False_False_False_level5, 'if_nl_preposition')

        df_False_False_False_False_True_level6 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_level6 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_level5.loc[idx]
            df_False_False_False_False_True_level6 = df_False_False_False_False_True_level6._append(row)

        for idx in false_index:
            row = df_False_False_False_False_level5.loc[idx]
            df_False_False_False_False_False_level6 = df_False_False_False_False_False_level6._append(row)

        df_False_False_False_False_True_level6 = df_False_False_False_False_True_level6.reset_index(drop=True)
        df_False_False_False_False_False_level6 = df_False_False_False_False_False_level6.reset_index(drop=True)

        # print(df_False_False_False_False_True_level6)
        # print(df_False_False_False_False_False_level6)

    #############################################################################

    ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_False_True_level6.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'


    ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE -> FALSE  ##########################

        columns_level6 = [ 'if_eng_preposition', 'if_nl_conjunction']

        for column_name in columns_level6:
            remainder, _, _ = self.test_column_remainder(df_False_False_False_False_False_level6, column_name)
            # print(remainder, column_name)

        _, true_index, false_index = self.test_column_remainder(df_False_False_False_False_False_level6, 'if_eng_preposition')

        df_False_False_False_False_False_True_level7 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_False_level7 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_False_level6.loc[idx]
            df_False_False_False_False_False_True_level7 = df_False_False_False_False_False_True_level7._append(row)

        for idx in false_index:
            row = df_False_False_False_False_False_level6.loc[idx]
            df_False_False_False_False_False_False_level7 = df_False_False_False_False_False_False_level7._append(row)

        df_False_False_False_False_False_True_level7 = df_False_False_False_False_False_True_level7.reset_index(drop=True)
        df_False_False_False_False_False_False_level7 = df_False_False_False_False_False_False_level7.reset_index(drop=True)

        # print(df_False_False_False_False_False_True_level7)
        # print(df_False_False_False_False_False_False_level7)

    ###################         level 6   FALSE -> FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_False_False_True_level7.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

    ###################         level 6   FALSE -> FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################

        _, true_index, false_index = self.test_column_remainder(df_False_False_False_False_False_False_level7, 'if_nl_conjunction')

        df_False_False_False_False_False_False_True_level8 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_False_False_level8 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_False_False_level7.loc[idx]
            df_False_False_False_False_False_False_True_level8 = df_False_False_False_False_False_False_True_level8._append(row)

        for idx in false_index:
            row = df_False_False_False_False_False_False_level7.loc[idx]
            df_False_False_False_False_False_False_False_level8 = df_False_False_False_False_False_False_False_level8._append(row)

        df_False_False_False_False_False_False_True_level8 = df_False_False_False_False_False_False_True_level8.reset_index(drop=True)
        df_False_False_False_False_False_False_False_level8 = df_False_False_False_False_False_False_False_level8.reset_index(drop=True)

        # print(df_False_False_False_False_False_False_True_level8)
        # print(df_False_False_False_False_False_False_False_level8)

    ###########         FALSE->

        for index, row in df_False_False_False_False_False_False_True_level8.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'

    ############

        for index, row in df_False_False_False_False_False_False_False_level8.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        cols = list(df.columns)
        cols = [cols[-1]] + cols[:-1]  # move last column to front
        cols = [cols.pop(0)] + cols  # move first column to second position
        df = df[cols]

        # print(type(df))
        return df


    def test_tree(self):
        pd.options.display.max_columns = None
        pd.options.display.max_rows = None
        df = self.read_file()
        df = self.if_eng_article(df)
        df = self.if_eng_conjunction(df)
        df = self.if_eng_preposition(df)
        df = self.if_nl_article(df)
        df = self.if_nl_conjunction(df)
        df = self.if_nl_preposition(df)
        df = self.if_eng_common(df)
        df['prediction'] = None

        ###################         level 2         ##########################

        true_index, false_index = self.true_false_indices(df, 'if_nl_article')


        df_True_level2 = pd.DataFrame(columns=df.columns)
        df_False_level2 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df.loc[idx]
            df_True_level2 = df_True_level2._append(row)

        for idx in false_index:
            row = df.loc[idx]
            df_False_level2 = df_False_level2._append(row)

        df_True_level2 = df_True_level2.reset_index(drop=True)
        df_False_level2 = df_False_level2.reset_index(drop=True)


        ###################         level 2   TRUE      ##########################

        true_index, false_index = self.true_false_indices(df_True_level2, 'if_nl_preposition')

        df_True_level3 = pd.DataFrame(columns=df.columns)
        df_False_level3 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_True_level2.loc[idx]
            df_True_level3 = df_True_level3._append(row)

        for idx in false_index:
            row = df_False_level2.loc[idx]
            df_False_level3 = df_False_level3._append(row)

        df_True_level3 = df_True_level3.reset_index(drop=True)
        df_False_level3 = df_False_level3.reset_index(drop=True)

        ###################         level 3   TRUE -> TRUE      ##########################

        for index, row in df_True_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'

        ###################         level 3   TRUE -> FALSE     ##########################

        for index, row in df_False_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        #############################################################################

        ###################         level 2   False     ##########################

        true_index, false_index = self.true_false_indices(df_False_level2, 'if_eng_article')



        df_False_True_level3 = pd.DataFrame(columns=df.columns)
        df_False_False_level3 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_level2.loc[idx]
            df_False_True_level3 = df_False_True_level3._append(row)

        for idx in false_index:
            row = df_False_level2.loc[idx]
            df_False_False_level3 = df_False_False_level3._append(row)

        df_False_True_level3 = df_False_True_level3.reset_index(drop=True)
        df_False_False_level3 = df_False_False_level3.reset_index(drop=True)


        ###################         level 3   FALSE -> TRUE    ##########################

        for index, row in df_False_True_level3.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        ###################         level 3   FALSE -> FALSE    ##########################

        true_index, false_index = self.true_false_indices(df_False_False_level3, 'if_eng_conjunction')

        df_False_False_True_level4 = pd.DataFrame(columns=df.columns)
        df_False_False_False_level4 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_level3.loc[idx]
            df_False_False_True_level4 = df_False_False_True_level4._append(row)

        for idx in false_index:
            row = df_False_False_level3.loc[idx]
            df_False_False_False_level4 = df_False_False_False_level4._append(row)

        df_False_False_True_level4 = df_False_False_True_level4.reset_index(drop=True)
        df_False_False_False_level4 = df_False_False_False_level4.reset_index(drop=True)



        ###################         level 3   FALSE -> FALSE -> TRUE   ##########################

        for index, row in df_False_False_True_level4.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        ###################         level 3   FALSE -> FALSE -> FALSE   ##########################

        true_index, false_index = self.true_false_indices(df_False_False_False_level4, 'if_eng_common')

        df_False_False_False_True_level5 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_level5 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_level4.loc[idx]
            df_False_False_False_True_level5 = df_False_False_False_True_level5._append(row)

        for idx in false_index:
            row = df_False_False_False_level4.loc[idx]
            df_False_False_False_False_level5 = df_False_False_False_False_level5._append(row)

        df_False_False_False_True_level5 = df_False_False_False_True_level5.reset_index(drop=True)
        df_False_False_False_False_level5 = df_False_False_False_False_level5.reset_index(drop=True)



        ###################         level 4   FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_True_level5.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE  ##########################

        true_index, false_index = self.true_false_indices(df_False_False_False_False_level5, 'if_nl_preposition')


        df_False_False_False_False_True_level6 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_level6 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_level5.loc[idx]
            df_False_False_False_False_True_level6 = df_False_False_False_False_True_level6._append(row)

        for idx in false_index:
            row = df_False_False_False_False_level5.loc[idx]
            df_False_False_False_False_False_level6 = df_False_False_False_False_False_level6._append(row)

        df_False_False_False_False_True_level6 = df_False_False_False_False_True_level6.reset_index(drop=True)
        df_False_False_False_False_False_level6 = df_False_False_False_False_False_level6.reset_index(drop=True)


        #############################################################################

        ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_False_True_level6.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'

        ###################         level 4   FALSE -> FALSE -> FALSE -> FALSE -> FALSE  ##########################


        true_index, false_index = self.true_false_indices(df_False_False_False_False_False_level6,
                                                                'if_eng_preposition')

        df_False_False_False_False_False_True_level7 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_False_level7 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_False_level6.loc[idx]
            df_False_False_False_False_False_True_level7 = df_False_False_False_False_False_True_level7._append(row)

        for idx in false_index:
            row = df_False_False_False_False_False_level6.loc[idx]
            df_False_False_False_False_False_False_level7 = df_False_False_False_False_False_False_level7._append(row)

        df_False_False_False_False_False_True_level7 = df_False_False_False_False_False_True_level7.reset_index(
            drop=True)
        df_False_False_False_False_False_False_level7 = df_False_False_False_False_False_False_level7.reset_index(
            drop=True)



        ###################         level 6   FALSE -> FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################

        for index, row in df_False_False_False_False_False_True_level7.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        ###################         level 6   FALSE -> FALSE -> FALSE -> FALSE -> FALSE -> TRUE  ##########################



        true_index, false_index = self.true_false_indices(df_False_False_False_False_False_False_level7,
                                                                'if_nl_conjunction')



        df_False_False_False_False_False_False_True_level8 = pd.DataFrame(columns=df.columns)
        df_False_False_False_False_False_False_False_level8 = pd.DataFrame(columns=df.columns)

        for idx in true_index:
            row = df_False_False_False_False_False_False_level7.loc[idx]
            df_False_False_False_False_False_False_True_level8 = df_False_False_False_False_False_False_True_level8._append(
                row)

        for idx in false_index:
            row = df_False_False_False_False_False_False_level7.loc[idx]
            df_False_False_False_False_False_False_False_level8 = df_False_False_False_False_False_False_False_level8._append(
                row)

        df_False_False_False_False_False_False_True_level8 = df_False_False_False_False_False_False_True_level8.reset_index(
            drop=True)
        df_False_False_False_False_False_False_False_level8 = df_False_False_False_False_False_False_False_level8.reset_index(
            drop=True)



        ###########         FALSE->

        for index, row in df_False_False_False_False_False_False_True_level8.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'nl'

        ############

        for index, row in df_False_False_False_False_False_False_False_level8.iterrows():
            sentence = row['sentence']
            if sentence in df['sentence'].tolist():
                idx = df.index[df['sentence'] == sentence].tolist()[0]
                df.loc[idx, 'prediction'] = 'en'

        cols = list(df.columns)
        cols = [cols[-1]] + cols[:-1]  # move last column to front
        cols = [cols.pop(0)] + cols  # move first column to second position
        df = df[cols]

        # print(type(df))
        return df


with open('best.model', "wb") as f:
    pickle.dump(Train, f)






