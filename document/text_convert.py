import numpy as np
import math

Document1 = "It is going to rain today."
Document2 = "Today I am not going outside."
Document3 = "I am going to watch the season premiere."

Doc = np.array([Document1, Document2, Document3])

doc1 = Document1.split(' ')
doc2 = Document2.split(' ')
doc3 = Document3.split(' ')

text_join = set(doc1).union(set(doc2))

dict_a = dict.fromkeys(text_join, 0)
print(dict_a)


for word in doc1:
    dict_a[word] += 1
    
dict_b = dict.fromkeys(text_join, 0)
for text_word in doc2:
    dict_b[text_word] =+ 1

def compute_term_frequency(word_dictionary, bag_of_words):
    term_frequency_dictionary = {}
    length_of_bag_of_words = len(bag_of_words)
    for word, count in word_dictionary.items():
        term_frequency_dictionary[word] = count / float(length_of_bag_of_words)
    return term_frequency_dictionary

tf = compute_term_frequency(dict_a, doc1)

def compute_inverse_document_frequency(full_doc_list):
    idf_dict = {}
    length_of_doc_list = len(full_doc_list)

    idf_dict = dict.fromkeys(full_doc_list[0].keys(), 0)
    for word, value in idf_dict.items():
        idf_dict[word] = math.log(length_of_doc_list / (float(value) + 1))

    return idf_dict

final_idf_dict = compute_inverse_document_frequency([dict_a, dict_b])
print(final_idf_dict)


