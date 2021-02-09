# Semi-supervised-Multi-level-neural-approach

We describe all the files that are present in our code below.
1. gen_augment_data.py: It generates augmented data for various proposed data
augmentation methods
2. main.py: It is used to run all the deep learning based methods including the
baselines and proposed approach after generating the augmented data.
3. neural_approaches.py: It involves training, prediction, training data creation and
transformation, loss function assignment, class imbalance correction, and more.
4. dlModels.py: It consists of the deep learning architectures for the proposed and
baseline methods
5. loadPreProc.py: It contains functions for data loading, preprocessing, and more.
6. sent_enc_embed.py : It generates sentence embeddings from BERT, USE, etc.
7. word_embed.py: It generates word embeddings from ELMo, GloVe, etc.
8. gen_batch_keras.py: It contains functions to generate batches of inputs for
training and testing.
9. arranging.py: It involves data loading for some auxiliary tasks and more.
10. evalMeasures.py: It comprises functions used for multi-label classification
evaluation.
11. rand_approach.py: It performs random label selection in accordance with the
normalized label frequencies of labels in the training data.
12. analysis_labels_per_post.py: It is used to select the samples and the associated
information in Table 5.
13. chart_class_wise_performance.py: It is used to plot class-wise F score.
14. TraditionalML_LP.py: It implements traditional machine learning methods.
15. bert_features: It is used to generate the tBERT embeddings.
16. bert_modelling: It have all the models related to BERT
17. bert_pretraining.py: It is used to pre-train the bert model using unlabeled
accounts of sexism.
18. deriving_confscores.py: It is used to derive the confidence scores for multi-level
training.
19. config_deep_learning.txt: It is a configuration file for the proposed methods and
deep learning baselines.
20. config_traditional_ML.txt: It is a configuration file for the traditional ML methods.

Tuned hyper-parameters_TSC.pdf: It contains all the hyperparameters.