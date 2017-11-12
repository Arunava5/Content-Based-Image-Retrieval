import os
import cv2
import numpy as np
import mahotas

low = 1
high = 1000

def img2feature(img,size = (32,32)):
    return cv2.resize(img,size).flatten().tolist()

def img2hist(img,bins = (8,8,8)):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv],[0,1,2],None,bins,[0,180,0,256,0,256])
    cv2.normalize(hist,hist)
    return hist.flatten().tolist()

def img2modihist(img,bins = (8,8,8)):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    features = []
    (h,w) = hsv.shape[:2]
    (cX,cY) = (int(w*0.5),int(h*0.5))
    segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),(0, cX, cY, h)]
    (axesX, axesY) = (int(w * 7/32), int(h * 7/32) )
    ellipMask = np.zeros(hsv.shape[:2], dtype = "uint8")
    cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
    for (startX, endX, startY, endY) in segments:
        cornerMask = np.zeros(hsv.shape[:2], dtype = "uint8")
        cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
        cornerMask = cv2.subtract(cornerMask, ellipMask)
        hist = cv2.calcHist([hsv],[0,1,2],cornerMask,bins,[0,180,0,256,0,256])
        cv2.normalize(hist,hist)
        hist = hist.flatten().tolist()
        features += hist    
    hist = cv2.calcHist([hsv],[0,1,2],ellipMask,bins,[0,180,0,256,0,256])
    cv2.normalize(hist,hist)
    hist = hist.flatten().tolist()
    features += hist
    return features

def img2modihist2(img,bins = (8,8,8)):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    features = []
    (h,w) = hsv.shape[:2]
    segments = [(0, w, 0, int(0.2*h)), (0, w, int(0.2*h), int(0.8*h)), (0, w, int(0.8*h), h)]
    for (startX, endX, startY, endY) in segments:
        cornerMask = np.zeros(hsv.shape[:2], dtype = "uint8")
        cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
        hist = cv2.calcHist([hsv],[0,1,2],cornerMask,bins,[0,180,0,256,0,256])
        cv2.normalize(hist,hist)
        hist = hist.flatten().tolist()
        features += hist    
    return features

def img2shape(img,radius):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return mahotas.features.zernike_moments(img_gray,radius)

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