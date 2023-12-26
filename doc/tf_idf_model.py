import numpy as np
import nltk
import pandas as pd
nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.tokenize import word_tokenize, sent_tokenize


Document1 = "It is going to rain today."
Document2 = "Today I am not going outside."
Document3 = "I am going to watch the season premiere."

Doc = np.array([Document1, Document2, Document3])

vector =  TfidfVectorizer()
cou_vetor = CountVectorizer()

tfd = cou_vetor.fit_transform(Doc)
tk = cou_vetor.get_feature_names_out()

matrix = tfd.todense()
text_list = matrix.tolist()
df  = pd.DataFrame(text_list, columns=tk)
print(df)
