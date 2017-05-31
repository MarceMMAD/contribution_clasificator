import Noun_extract

def calculate_vector(text):
    current_nouns = Noun_extract.get_nouns(text)
    current_bow = Noun_extract.transform_to_bow(current_nouns)
    return current_bow

def cast_vector(text):
    current_nouns = Noun_extract.get_nouns(text)
    current_fit = Noun_extract.transform_to_fit(current_nouns)
    return current_fit