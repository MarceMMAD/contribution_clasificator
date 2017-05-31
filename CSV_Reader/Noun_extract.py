import nltk
from nltk import FreqDist
import scipy
from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()

def get_nouns(text):
    text_with_no_new_lines = text.replace('\n',' ')
    tokens = nltk.word_tokenize(text_with_no_new_lines)
    pos_tag = nltk.pos_tag(tokens)
    nouns = [t[0] for t in pos_tag if t[1]=='NN' or t[1] =='NNS']
    ocur = FreqDist(nouns)
    most = ocur.most_common()
    return ocur

def transform_to_bow(dict_list):
    vector = vec.fit_transform(dict_list)
    names = vec.get_feature_names()
    return vector

def transform_to_fit(text_list):
    fit = vec.transform(text_list)
    return fit
#x = get_nouns('What is the airspeed velocity of an unladen swallow?')

