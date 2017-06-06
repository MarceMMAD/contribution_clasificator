import Input_reader
import Noun_extract
import corpus_load
from sklearn import metrics as me
from scipy import spatial
import nltk



file_name_location = 'C:\\Users\\b.balcerzak\\contribution_clasificator\\test_new_1.csv'
submission_file = 'C:\\Users\\b.balcerzak\\contribution_clasificator\\test_new_2.csv'


submission_list = Input_reader.csv_data_extract(submission_file)
# Transforming the corpus into a noun frequency representation
My_input = Input_reader.csv_data_extract(file_name_location)
My_ouput = []
for new_submission in submission_list:
    current_similarity = 0.0
    current_category = ''
    present_submission = new_submission[0].replace('\n',' ')
#this will be moved to a specific file corpus_load.py
    for submission in My_input:
        submission_bow = corpus_load.calculate_vector(submission[0])
        test = corpus_load.cast_vector(new_submission[0])
        x_submission_bow = corpus_load.calculate_vector(new_submission[0])
        x_test = corpus_load.cast_vector(submission[0])
#        print 'test'
        try:
            similarity_1 = float(1- spatial.distance.cosine(test.toarray(),submission_bow.toarray()))
            similarity_2 = float(1- spatial.distance.cosine(x_test.toarray(),x_submission_bow.toarray()))
            similarity = similarity_1/similarity_2
            if similarity >0.0 and similarity > current_similarity:
                current_similarity = similarity
                current_category = submission[1]
        except:
            print 'error'
#    print 'becki'
    delimiter = ';'
    print current_category,delimiter ,new_submission[1], delimiter, current_similarity, present_submission
#    new_submission[1] = current_category
#    My_input.append(new_submission)
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
