import Input_reader
import Noun_extract
import corpus_load
from sklearn import metrics as me
from scipy import spatial

file_name_location = 'C:\\Users\\b.balcerzak\\contribution_clasificator\\Contribution_Corpus.csv'

submission_list = 'The city of vallejo should do something about the trash.'
# Transforming the corpus into a noun frequency representation
My_input = Input_reader.csv_data_extract(file_name_location)
My_ouput = []
current_similarity = 0.0
current_category = ''
#this will be moved to a specific file corpus_load.py
for submission in My_input:
    submission_bow = corpus_load.calculate_vector(submission[0])
    test = corpus_load.cast_vector(submission_list)
    try:
        similarity = float(1- spatial.distance.cosine(test.toarray(),submission_bow.toarray()))
        if similarity >0.0 and similarity > current_similarity:
            current_similarity = similarity
            current_category = submission[1]
    except:
        None
print submission_list, current_category, current_similarity
#  print spatial.distance.euclidean(test,row)

#print My_ouput
#similarity =[]
#for each_submission in My_ouput:
#    sub_dict=Noun_extract.get_dist(Noun_extract.get_nouns(submission_list[0]))
#    word_set_1 = [t[0] for t in sub_dict]
#    word_set_2 = [c[0] for c in each_submission[1]]
#    sim = set(word_set_1) & set(word_set_2)
#    similarity.append(len(sim))
#print similarity


#   here happens the similarity and matching
#   here happens the adddition of the submission to the corpus.
