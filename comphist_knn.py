from sklearn.neighbors import KNeighborsClassifier
import csv   
from read_csv import readfile

file_trainraw = open("Training_Data/trainraw.csv","r")
file_trainhist = open("Training_Data/trainhist.csv","r")
file_trainmodihist = open("Training_Data/trainmodihist.csv","r")
file_trainmodihist2 = open("Training_Data/trainmodihist2.csv","r")
file_trainshape = open("Training_Data/trainshape.csv","r")
file_testraw = open("Testing_Data/testraw.csv","r")
file_testhist = open("Testing_Data/testhist.csv","r")
file_testmodihist = open("Testing_Data/testmodihist.csv","r")
file_testmodihist2 = open("Testing_Data/testmodihist2.csv","r")
file_testshape = open("Testing_Data/testshape.csv","r")

curr_data = []

print("Using KNN Classifier.....\n")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)

print("Evaluating raw pixel accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainraw),10000)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testraw),10000)]
accuracy_raw = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
                          [ int(row[0]) for row in curr_data ])

print("Raw pixel accuracy : {:.2f}%\n".format(accuracy_raw * 100))

print("Evaluating histogram accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainhist),10000)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testhist),10000)]
accuracy_hist = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
                           [ int(row[0]) for row in curr_data ])

print("Histogram accuracy : {:.2f}%\n".format(accuracy_hist * 100))

print("Evaluating Modified histogram accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainmodihist),10000)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testmodihist),10000)]
accuracy_modihist = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

print("Modified Histogram accuracy : {:.2f}%\n".format(accuracy_modihist * 100))

print("Evaluating Modified histogram2 accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainmodihist2),10000)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testmodihist2),10000)]
accuracy_modihist2 = clf.score( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

print("Modified Histogram2 accuracy : {:.2f}%\n".format(accuracy_modihist2 * 100))

print("Evaluating shape accuracy...")

curr_data = [row for row in readfile(csv.reader(file_trainshape),10000)]
clf.fit( [ [ float(x) for x in row[1:] ] for row in curr_data ],
           [ int(row[0]) for row in curr_data ])

curr_data = [row for row in readfile(csv.reader(file_testshape),10000)]
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