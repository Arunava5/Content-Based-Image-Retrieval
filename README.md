# Content-Based-Image-Retrieval
A <b>CBIR</b> system which takes a query image as input, matches it with the database and returns the best matches.

Steps to run the program:

1. Run <i>feature_gen.py</i> ( Generates the feature vectors of all the images in the dataset and stores them in a new folder <b>Feature_Vectors(low-high)</b> )
2. Run <i>train_test_gen.py</i> ( Generates the training data and the testing data for machine learning and stores them in new folders <b>Training_data(low-high)</b> and <b>Testing_data(low-high)</b> respectively )
3. Run <i>comphist_knn.py</i> ( Feeds the training data to a KNN Classifier and then tests it against the testing data, display accuracy score in console )

(If you want to test the program for a specific subset of images, then update the <i>low</i> and <i>high</i> values in the above three files)

(<i>low</i> = image_number of first image in the dataset, <i>high</i> = image_number of last image in the dataset)
