# Language-Classifier

A Web-app for Language classification which takes input from user to classify whther the input sentence is English language or Dutch Language using Decision Tree and Adaboost algorithm.




Features:

    if_nl_article:
        All the common dutch articles are used
        ['de', 'het', 'een']
        if any of these are present then the feature is True, else False

    if_nl_conjunction:
        All the common dutch conjunctions are used
        ['en', 'of', 'maar', 'dus', 'ofwel', 'noch', 'hoewel', 'omdat', 'sinds', 'tenzij', 'terwijl',
                            'waar', 'indien', 'zodra', 'eerder', 'dan', 'alsof', 'alsook']
       if any of these are present then the feature is True, else False

    if_nl_preposition:
        All the common dutch prepositions are used.
        ['aan', 'achter', 'bij', 'binnen', 'buiten', 'door', 'in', 'langs', 'met', 'na', 'naar', 'onder',
                            'op', 'over', 'tegen', 'tussen', 'uit', 'van', 'voor', 'onder', 'langs', 'rond', 'om', 'tot']
        if any of these are present then the feature is True, else False

    if_eng_article:
        All the common english articles are used.
        ['a', 'an', 'the']
        if any of these are present then the feature is True, else False


    if_eng_preposition:
        All the common english prepositions are used.
        ['about', 'above', 'across', 'after', 'against', 'along', 'amid', 'amidst', 'among', 'amongst',
                            'around', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond',
                            'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'for', 'from', 'in',
                            'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past',
                            'regarding', 'round', 'since', 'through', 'throughout', 'to', 'toward', 'towards', 'under',
                            'underneath', 'until', 'till', 'up', 'upon', 'with', 'within', 'without']
        if any of these are present then the feature is True, else False

    if_eng_conjunction:
        All the common english conjunctions are used.
        ['and', 'or', 'but', 'so', 'for', 'yet', 'nor', 'although', 'because', 'since', 'unless', 'while',
                            'whereas', 'if']
        if any of these are present then the feature is True, else False

    if_eng_common:
        All the common english common words are used.
        ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
                            'this', 'that', 'these', 'those', 'here', 'there', 'now', 'then', 'always', 'never',
                            'sometimes', 'often', 'rarely', 'quickly', 'slowly', 'easily', 'hard', 'well', 'better',
                            'best', 'worse', 'worst', 'more', 'most', 'least', 'all', 'some', 'none', 'many', 'few',
                            'every', 'any', 'such', 'no', 'other', 'another', 'enough', 'even',
                            'always', 'never', 'sometimes', 'often', 'rarely', 'quickly', 'slowly', 'easily', 'hard', 'well', 'better', 'best',
                             'worse', 'worst', 'more', 'most', 'least', 'all', 'some', 'none', 'many']
        if any of these are present then the feature is True, else False


Decision tree:

for every level of the tree i calculated the remainder as showed in the class and then the feature with least remainder value was then used as the next level of the DT.
features = 7
Depth = 8

When ran on the given test.dat test examples, i got all the right predictions. 100% accuracy with the predictions on the given file.

Adaboost:

i tested with 4, 6, 7, 10 stumps but got a lot of wrong predictions.
then i tried running this adaboost algorithm for 100 stumps and then got a much better result with better predictions.

When ran on the given test.dat test examples, i got 8 / 10 right predictions. 80% accuracy with the predictions on the given file.
