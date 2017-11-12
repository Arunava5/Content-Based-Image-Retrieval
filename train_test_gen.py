import os
from sklearn.model_selection import train_test_split
import csv
from read_csv import readfile

low = 1
high = 1000

folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
training_folder = "Training_Data(" + str(low) + "-" + str(high) + ")"
testing_folder = "Testing_Data(" + str(low) + "-" + str(high) + ")"

os.mkdir(training_folder)
os.mkdir(testing_folder)

file_raw = open(folder_name+"/raw_features.csv","r")
file_hist = open(folder_name+"/hist_features.csv","r")
file_modihist = open(folder_name+"/modihist.csv","r")
file_modihist2 = open(folder_name+"/modihist2.csv","r")
file_zernike = open(folder_name+"/zernike.csv","r")

file_trainraw = open(training_folder+"/trainraw.csv","w")
file_trainhist = open(training_folder+"/trainhist.csv","w")
file_trainmodihist = open(training_folder+"/trainmodihist.csv","w")
file_trainmodihist2 = open(training_folder+"/trainmodihist2.csv","w")
file_trainshape = open(training_folder+"/trainshape.csv","w")

file_testraw = open(testing_folder+"/testraw.csv","w")
file_testhist = open(testing_folder+"/testhist.csv","w")
file_testmodihist = open(testing_folder+"/testmodihist.csv","w")
file_testmodihist2 = open(testing_folder+"/testmodihist2.csv","w")
file_testshape = open(testing_folder+"/testshape.csv","w")

reader_raw = csv.reader(file_raw)
reader_hist = csv.reader(file_hist)
reader_modihist = csv.reader(file_modihist)
reader_modihist2 = csv.reader(file_modihist2)
reader_zernike = csv.reader(file_zernike)

raw_rows = []
hist_rows = []
modihist_rows = []
modihist2_rows = []
zernike_rows = []

print("Creating Training & Testing data.....")

high += 1
step = (high-low)//10

for i in range(low,high):
    if (i-low+1) % step == 0:
        print("%d%% complete\n"%((i-low+1)//step*10))
    raw_rows = readfile(reader_raw,100)
    hist_rows = readfile(reader_hist,100)
    modihist_rows = readfile(reader_modihist,100)
    modihist2_rows = readfile(reader_modihist2,100)
    zernike_rows = readfile(reader_zernike,100)    
              
    (trainrawfexp,testrawfexp,trainrawlexp,testrawlexp) = train_test_split(
                                         [ row[2:] for row in raw_rows ],
                                         [ row[1] for row in raw_rows ],
                                         test_size = 0.2,random_state = 42)
    (trainhistfexp,testhistfexp,trainhistlexp,testhistlexp) = train_test_split(
                                         [ row[2:] for row in hist_rows ],
                                         [ row[1] for row in hist_rows ],
                                         test_size = 0.2,random_state = 42)
    (trainmodihistfexp,testmodihistfexp,trainmodihistlexp,testmodihistlexp) = train_test_split(
                                         [ row[2:] for row in modihist_rows ],
                                         [ row[1] for row in modihist_rows ],
                                         test_size = 0.2,random_state = 42)
    (trainmodihist2fexp,testmodihist2fexp,trainmodihist2lexp,testmodihist2lexp) = train_test_split(
                                         [ row[2:] for row in modihist2_rows ],
                                         [ row[1] for row in modihist2_rows ],
                                         test_size = 0.2,random_state = 42)
    (trainshapefexp,testshapefexp,trainshapelexp,testshapelexp) = train_test_split(
                                         [ row[2:] for row in zernike_rows ],
                                         [ row[1] for row in zernike_rows ],
                                         test_size = 0.2,random_state = 42)
    for (f,l) in zip(trainrawfexp,trainrawlexp):
        file_trainraw.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(trainhistfexp,trainhistlexp):
        file_trainhist.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(trainmodihistfexp,trainmodihistlexp):
        file_trainmodihist.write("%s,%s\n"%(l,",".join(f)))    
    for (f,l) in zip(trainmodihist2fexp,trainmodihist2lexp):
        file_trainmodihist2.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(trainshapefexp,trainshapelexp):
        file_trainshape.write("%s,%s\n"%(l,",".join(f)))
        
    for (f,l) in zip(testrawfexp,testrawlexp):
        file_testraw.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(testhistfexp,testhistlexp):
        file_testhist.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(testmodihistfexp,testmodihistlexp):
        file_testmodihist.write("%s,%s\n"%(l,",".join(f)))    
    for (f,l) in zip(testmodihist2fexp,testmodihist2lexp):
        file_testmodihist2.write("%s,%s\n"%(l,",".join(f)))
    for (f,l) in zip(testshapefexp,testshapelexp):
        file_testshape.write("%s,%s\n"%(l,",".join(f)))        

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

file_raw.close()
file_hist.close()
file_modihist.close()
file_modihist2.close()
file_zernike.close()

print("Training & Testing data created successfully!")