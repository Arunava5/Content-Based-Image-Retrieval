# Content-Based-Image-Retrieval
A CBIR system which takes a query image as input,matches it with the database and returns the best matches.

Steps to run the program:

1. Run feature_gen.py (Generates the feature vectors of all the images in the dataset)
2. Run train_test_gen.py (Generates the training data and the testing data for machine learning)
3. Run comphist_knn.py (Feeds the training data to a KNN Classifier and then tests it against the testing data)