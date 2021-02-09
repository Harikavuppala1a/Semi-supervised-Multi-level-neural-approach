import pickle
from loadPreProc import *
import sys
import copy
import collections



def derive_confscores(data_dict,data_dict_original,conf_score_filename_list,map_ind,save_folder_name):

    with open(conf_score_filename_list[-1], 'rb') as conf_data:
            conf_scores_array,initial_train_en_ind,semisup_train_end_ind = pickle.load(conf_data)

    derived_conf_scores_array = np.ones([data_dict['val_en_ind'], data_dict['NUM_CLASSES']])

    merge_categories_list = []
    for i in range(data_dict_original['NUM_CLASSES']):
        orig_label = data_dict_original['FOR_LMAP'][i]
        merge_categories_list.append(data_dict['LABEL_MAP'][orig_label])

    for lab_list_ind,label_list in enumerate(conf_scores_array[initial_train_en_ind:semisup_train_end_ind]):

        map_dict = {}
        for a, b in zip(merge_categories_list, label_list):
            map_dict.setdefault(a, []).append(b)

        sort_map_dict = collections.OrderedDict(sorted(map_dict.items()))
        scores = []
        for key in sort_map_dict:
            scores.append(sum(sort_map_dict[key])/len(sort_map_dict[key]))

        derived_conf_scores_array[lab_list_ind+initial_train_en_ind] = scores

    with open(conf_score_filename_list[map_ind], 'wb') as conf_data:
        pickle.dump([derived_conf_scores_array,initial_train_en_ind,semisup_train_end_ind], conf_data)    


  

