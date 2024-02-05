
# # Try to include * as an identifier

"""
Report the error to the end user

Test both the application and the algorithm thoroughly

create a class for each operator; learn how to create dunder functions
"""


class Tokenizer:
    """
    returns a tuple that contains another tuple of lexicon and type
    """

    @staticmethod
    def tokenize(text):
        tokens = list(text)
        lexicons = []
        token = ""
        i = 0
        while i < len(tokens):
            if tokens[i].isspace():
                if token:
                    Tokenizer.classify_token(token, lexicons)
                    token = ""
            elif tokens[i] in {'+'}:
                if token:
                    Tokenizer.classify_token(token, lexicons)
                    token = ""
                lexicons.append((tokens[i], "operator"))
            else:
                token += tokens[i]
                print(token)
            i += 1

        if token:
            Tokenizer.classify_token(token, lexicons)

        return lexicons

    
    @staticmethod
    def classify_token(token, lexicons):
        if token.isdigit() or (token.replace('.', '', 1 ).isdigit() and token.count('.') == 1): # validate this method
            lexicons.append((Number(token), Number))
        else:
            lexicons.append((token, "error"))


    @classmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


class Number:
    def __init__(self, value: int, *args, **kwargs):
        if self.is_number(value):
            self.value = value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return self.value


    def __add__(self, x: int):
        return Number(self.value + x.value)

    @staticmethod        
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False



if __name__ == "__main__":
    # y = Number(2) + Number(3)
    # print(y.value)

    print(Tokenizer.tokenize("2+    3"))

# class Addition:
    
#     def __repr__(self):
#         return +
