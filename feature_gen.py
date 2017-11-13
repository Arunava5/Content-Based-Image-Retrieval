import os
import cv2
from img_descriptors import *

low = 1
high = 1000

print("Creating Feature Vectors.....\n")

folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
os.mkdir(folder_name)

file_raw = open(folder_name+"/raw_features.csv","w")
file_hist = open(folder_name+"/hist_features.csv","w")
file_modihist = open(folder_name+"/modihist.csv","w")
file_modihist2 = open(folder_name+"/modihist2.csv","w")
file_zernike = open(folder_name+"/zernike.csv","w")

high += 1
step = (high - low)//10

for i in range(low,high):
    if (i-low+1) % step == 0:
        print("%d%% complete\n"%((i-low+1)//step*10))
    filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(i) + ".jpg"
    label = ((i-1)//100) + 1
    image = cv2.imread(filepath)
    
    raw = img2feature(image)
    raw = [str(i) for i in raw]
    hist = img2hist(image)
    hist = [str(i) for i in hist]
    modihist = img2modihist(image)
    modihist = [str(i) for i in modihist]
    modihist2 = img2modihist2(image)
    modihist2 = [str(i) for i in modihist2]
    zernike = img2shape(image,21)
    zernike = [str(i) for i in zernike]
    
    file_raw.write("%s,%s,%s\n"%(str(i),str(label),",".join(raw)))
    file_hist.write("%s,%s,%s\n"%(str(i),str(label),",".join(hist)))
    file_modihist.write("%s,%s,%s\n"%(str(i),str(label),",".join(modihist)))
    file_modihist2.write("%s,%s,%s\n"%(str(i),str(label),",".join(modihist2)))
    file_zernike.write("%s,%s,%s\n"%(str(i),str(label),",".join(zernike)))      
    
file_raw.close()
file_hist.close()
file_modihist.close()
file_modihist2.close()
file_zernike.close()

print("Feature Vectors created successfully!")