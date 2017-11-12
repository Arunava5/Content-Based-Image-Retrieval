# Content-Based-Image-Retrieval
A CBIR system which takes a query image as input,matches it with the database and returns the best matches.

Steps to run the program:

1. Run feature_gen.py (Generates the feature vectors of all the images in the dataset and stores them in a new folder "Feature_Vectors(low-high)")
2. Run train_test_gen.py (Generates the training data and the testing data for machine learning and stores them in new folders "Training_data(low-high)" and "Testing_data(low-high)" respectively)
3. Run comphist_knn.py (Feeds the training data to a KNN Classifier and then tests it against the testing data, display accuracy score in console)

(If you want to test the program for a specific subset of images, thn update the "low" and "high" values in the above three files)
(low = image_number of first image in the dataset, high = image_number of last image in the dataset)