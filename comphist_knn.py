from sklearn.neighbors import KNeighborsClassifier
import csv   
from read_csv import readfile


low = 1
high = 10000

training_folder = "Training_Data(" + str(low) + "-" + str(high) + ")"
testing_folder = "Testing_Data(" + str(low) + "-" + str(high) + ")"

file_trainraw = open(training_folder+"/trainraw.csv","r")
file_trainhist = open(training_folder+"/trainhist.csv","r")
file_trainmodihist = open(training_folder+"/trainmodihist.csv","r")
file_trainmodihist2 = open(training_folder+"/trainmodihist2.csv","r")
file_trainshape = open(training_folder+"/trainshape.csv","r")

file_testraw = open(testing_folder+"/testraw.csv","r")
file_testhist = open(testing_folder+"/testhist.csv","r")
file_testmodihist = open(testing_folder+"/testmodihist.csv","r")
file_testmodihist2 = open(testing_folder+"/testmodihist2.csv","r")
file_testshape = open(testing_folder+"/testshape.csv","r")

curr_data = []

high += 1
no_of_images = high - low

print("Using KNN Classifier.....\n")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)

print("Evaluating raw pixel accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainraw),no_of_images)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testraw),no_of_images)]
accuracy_raw = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
                          [ int(row[0]) for row in curr_data ])

print("Raw pixel accuracy : {:.2f}%\n".format(accuracy_raw * 100))

print("Evaluating histogram accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainhist),no_of_images)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testhist),no_of_images)]
accuracy_hist = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
                           [ int(row[0]) for row in curr_data ])

print("Histogram accuracy : {:.2f}%\n".format(accuracy_hist * 100))

print("Evaluating Modified histogram accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainmodihist),no_of_images)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testmodihist),no_of_images)]
accuracy_modihist = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

print("Modified Histogram accuracy : {:.2f}%\n".format(accuracy_modihist * 100))

print("Evaluating Modified histogram2 accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainmodihist2),no_of_images)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testmodihist2),no_of_images)]
accuracy_modihist2 = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

print("Modified Histogram2 accuracy : {:.2f}%\n".format(accuracy_modihist2 * 100))

print("Evaluating shape accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainshape),no_of_images)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testshape),no_of_images)]
accuracy_shape = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

print("Shape accuracy : {:.2f}%".format(accuracy_shape * 100))

file_trainraw.close()
file_trainhist.close()
file_trainmodihist.close()
file_trainmodihist2.close()
file_trainshape.close()
file_testraw.close()
file_testhist.close()
file_testmodihist.close()
file_testmodihist2.close()
file_testshape.close()

print("\nDone!")