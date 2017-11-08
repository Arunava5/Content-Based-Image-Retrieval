from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import cv2
import numpy as np
import mahotas

def img2feature(img,size = (32,32)):
    return cv2.resize(img,size).flatten()

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
    (axesX, axesY) = (int(w * 3/8), int(h * 3/8) )
    ellipMask = np.zeros(hsv.shape[:2], dtype = "uint8")
    cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)
    for (startX, endX, startY, endY) in segments:
        cornerMask = np.zeros(hsv.shape[:2], dtype = "uint8")
        cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
        cornerMask = cv2.subtract(cornerMask, ellipMask)
        hist = cv2.calcHist([hsv],[0,1,2],cornerMask,bins,[0,180,0,256,0,256])
        cv2.normalize(hist,hist)
        hist = hist.flatten()
        for x in hist:
            features.append(x)
        
    hist = cv2.calcHist([hsv],[0,1,2],ellipMask,bins,[0,180,0,256,0,256])
    cv2.normalize(hist,hist)
    hist = hist.flatten()
    for x in hist:
        features.append(x)
    return features

def img2shape(img,radius):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return mahotas.features.zernike_moments(img_gray,radius).tolist()

print("Describing Images...")

rawimages = []
histograms = []
modihistograms = []
combihistograms = []
labels = []
shapes = []

for i in range(1,10001):
    if i % 1000 == 0:
        print(i)
    filepath = "Corel10K/" + str(i) + ".jpg"
    label = ((i-1)//100) + 1
    image = cv2.imread(filepath)
    
    raw = img2feature(image)
    hist = img2hist(image)
    modihist = img2modihist(image)
    zernike = img2shape(image,21)
    
    rawimages.append(raw)
    histograms.append(hist)
    modihistograms.append(modihist)
    combihistograms.append(modihist+zernike)
    shapes.append(zernike)
    labels.append(label)
    
'''   
(trainrawf,testrawf,trainrawl,testrawl) = train_test_split(
                                          rawimages,labels,test_size = 0.2,random_state = 42)
(trainhistf,testhistf,trainhistl,testhistl) = train_test_split(
                                          histograms,labels,test_size = 0.2,random_state = 42)
(trainmodihistf,testmodihistf,trainmodihistl,testmodihistl) = train_test_split(
                                          modihistograms,labels,test_size = 0.2,random_state = 42)
(trainshapef,testshapef,trainshapel,testshapel) = train_test_split(
                                          shapes,labels,test_size = 0.2,random_state = 42)
'''

(trainrawf,testrawf,trainrawl,testrawl) = ([],[],[],[])
(trainhistf,testhistf,trainhistl,testhistl) = ([],[],[],[])
(trainmodihistf,testmodihistf,trainmodihistl,testmodihistl) = ([],[],[],[])
(traincombihistf,testcombihistf,traincombihistl,testcombihistl) = ([],[],[],[])
(trainshapef,testshapef,trainshapel,testshapel) = ([],[],[],[])

for i in range(100):
    start = i*100;
    end = (i+1)*100;
    (trainrawfexp,testrawfexp,trainrawlexp,testrawlexp) = train_test_split(
                                         rawimages[start:end],labels[start:end],test_size = 0.2,random_state = 42)
    (trainhistfexp,testhistfexp,trainhistlexp,testhistlexp) = train_test_split(
                                         histograms[start:end],labels[start:end],test_size = 0.2,random_state = 42)
    (trainmodihistfexp,testmodihistfexp,trainmodihistlexp,testmodihistlexp) = train_test_split(
                                         modihistograms[start:end],labels[start:end],test_size = 0.2,random_state = 42)
    (traincombihistfexp,testcombihistfexp,traincombihistlexp,testcombihistlexp) = train_test_split(
                                         combihistograms[start:end],labels[start:end],test_size = 0.2,random_state = 42)
    (trainshapefexp,testshapefexp,trainshapelexp,testshapelexp) = train_test_split(
                                          shapes[start:end],labels[start:end],test_size = 0.2,random_state = 42)

    trainrawf += trainrawfexp
    testrawf += testrawfexp
    trainrawl += trainrawlexp
    testrawl += testrawlexp
    trainhistf += trainhistfexp
    testhistf += testhistfexp
    trainhistl += trainhistlexp
    testhistl += testhistlexp
    trainmodihistf += trainmodihistfexp
    testmodihistf += testmodihistfexp
    trainmodihistl += trainmodihistlexp
    testmodihistl += testmodihistlexp
    traincombihistf += traincombihistfexp
    testcombihistf += testcombihistfexp
    traincombihistl += traincombihistlexp
    testcombihistl += testcombihistlexp    
    trainshapef += trainshapefexp
    testshapef += testshapefexp
    trainshapel += trainshapelexp
    testshapel += testshapelexp        
    
'''
count_label = [0] * 101
minc = 1000
maxc = 0
for i in range(len(trainrawl)):
    count_label[trainrawl[i]] += 1
for i in range(1,101):
    print("%d -> %d"%(i,count_label[i]))
    minc = min(minc,count_label[i])
    maxc = max(maxc,count_label[i])    
print(minc)
print(maxc)    
'''
print("Evaluating raw pixel accuracy...")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)
clf.fit(trainrawf,trainrawl)
accuracy_raw = clf.score(testrawf,testrawl)
print("Raw pixel accuracy : {:.2f}%".format(accuracy_raw * 100))
print()
print("Evaluating histogram accuracy...")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)
clf.fit(trainhistf,trainhistl)
accuracy_hist = clf.score(testhistf,testhistl)
print("Histogram accuracy : {:.2f}%".format(accuracy_hist * 100))
print()
print("Evaluating Modified histogram accuracy...")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)
clf.fit(trainmodihistf,trainmodihistl)
accuracy_modihist = clf.score(testmodihistf,testmodihistl)
print("Modified Histogram accuracy : {:.2f}%".format(accuracy_modihist * 100))
print()
print("Evaluating Combined histogram accuracy...")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)
clf.fit(traincombihistf,traincombihistl)
accuracy_combihist = clf.score(testcombihistf,testcombihistl)
print("Combined Histogram accuracy : {:.2f}%".format(accuracy_combihist * 100))
print()
print("Evaluating shape accuracy...")
clf = KNeighborsClassifier(n_neighbors = 1,n_jobs = -1)
clf.fit(trainshapef,trainshapel)
accuracy_shape = clf.score(testshapef,testshapel)
print("Shape accuracy : {:.2f}%".format(accuracy_shape * 100))