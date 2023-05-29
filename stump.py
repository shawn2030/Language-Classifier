class Stump:

    def __init__(self, column_name = None, value = None, alpha = None):
        self.column_name = column_name
        self.value = value
        self.alpha = alpha
        # self.left = None
        # self.right = None

    def create_stump(self):

        if self.column_name == 'if_nl_article':
            if self.value == True:
                return -1
            elif self.value == False:
                return 1

        if self.column_name == 'if_nl_preposition':
            if self.value == True:
                return -1
            elif self.value == False:
                return 1

        if self.column_name == 'if_nl_conjunction':
            if self.value == True:
                return -1
            elif self.value == False:
                return 1

        if self.column_name == 'if_eng_article':
            if self.value == True:
                return 1
            elif self.value == False:
                return -1

        if self.column_name == 'if_eng_conjunction':
            if self.value == True:
                return 1
            elif self.value == False:
                return -1

        if self.column_name == 'if_eng_common':
            if self.value == True:
                return 1
            elif self.value == False:
                return -1

        if self.column_name == 'if_eng_preposition':
            if self.value == True:
                return 1
            elif self.value == False:
                return -1