import re

text = ' (to love is to destroy, and to be loved, is to be "the" one <destroyed>} '

def remove_punctuations(text):
    punctuation = re.compile(r'[{};():,."/<>-]')
    text = punctuation.sub(' ', text)
    return text

remove_text = remove_punctuations(text)
