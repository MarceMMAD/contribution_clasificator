import nltk
from nltk import FreqDist
def get_nouns(text):
    text_with_no_new_lines = text.replace('\n',' ')
    tokens = nltk.word_tokenize(text_with_no_new_lines)
    pos_tag = nltk.pos_tag(tokens)
    nouns = [t[0] for t in pos_tag if t[1]=='NN' or t[1] =='NNS']
    return nouns

def get_dist(list):
    ocur = FreqDist(list)
    return ocur.most_common()
#x = get_nouns('What is the airspeed velocity of an unladen swallow?')

