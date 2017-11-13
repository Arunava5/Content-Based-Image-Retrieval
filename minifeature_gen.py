import os
import cv2
from img_descriptors import img2modihist

def gen_dataset(low,high):

    print("Creating Feature Vectors.....\n")

    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    os.mkdir(folder_name)

    file_seghist = open(folder_name+"/seghist.csv","w")

    high += 1
    step = (high - low)//10

    for i in range(low,high):
        if (i-low+1) % step == 0:
            print("%d%% complete\n"%((i-low+1)//step*10))
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(i) + ".jpg"
        image = cv2.imread(filepath)
    
        modihist = img2modihist(image)
        modihist = [str(i) for i in modihist]
    
        file_seghist.write("%s,%s\n"%(str(i),",".join(modihist)))     
    
    file_seghist.close()

    print("Feature Vectors created successfully!")