import Input_reader
import Noun_extract
file_name_location = 'C:\\Users\\b.balcerzak\\contribution_clasificator\\Contribution_Corpus.csv'
submission_list = ['Our teens make bad choices, based on their flawed logic']
# Transforming the corpus into a noun frequency representation
My_input = Input_reader.csv_data_extract(file_name_location)
My_ouput = []

#this will be moved to a specific file corpus_load.py
for submission in My_input:
    current_text = submission[0]
    category = submission[1]
    current_nouns = Noun_extract.get_nouns(current_text)
    current_dist = Noun_extract.get_dist(current_nouns)
    current_vector = [category, current_dist]
    My_ouput.append(current_vector)

#print My_ouput
similarity =[]
for each_submission in My_ouput:
    sub_dict=Noun_extract.get_dist(Noun_extract.get_nouns(submission_list[0]))
    word_set_1 = [t[0] for t in sub_dict]
    word_set_2 = [c[0] for c in each_submission[1]]
    sim = set(word_set_1) & set(word_set_2)
    similarity.append(len(sim))
print similarity


#   here happens the similarity and matching
#   here happens the adddition of the submission to the corpus.
