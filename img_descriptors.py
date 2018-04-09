import cv2
import numpy as np
import mahotas
import pywt 
from skimage.feature import greycomatrix as gc
from skimage.feature import greycoprops as gp

def img2feature(img,size = (32,32)):
    return cv2.resize(img,size).flatten().tolist()

def img2hist(img,bins = (16,7,7)):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv],[0,1,2],None,bins,[0,180,0,256,0,256])
    cv2.normalize(hist,hist)
    return hist.flatten().tolist()

def img2modihist(img,bins = (11,8,9)):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    features = []
    (h,w) = hsv.shape[:2]
    (cX,cY) = (int(w*0.5),int(h*0.5))
    segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),(0, cX, cY, h)]
    (axesX, axesY) = (int(w/5), int(h/5) )
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

def img2modihist2(img,bins = (16,7,7)):
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

def w2d(img, mode='haar', level=1):
    imArray = cv2.imread(img)
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_BGR2GRAY )
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255;
    # compute coefficients 
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)  
    coeffs_H[0] *= 0;  

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)
    return imArray_H

def texcal(img,modihist):
    grey = gc(img,[1],[0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2, 5*np.pi/8, 3*np.pi/4, 7*np.pi/8],levels = 256, normed = True)
    contrast = gp(grey,'contrast')
    energy = gp(grey,'energy')
    correlation = gp(grey,'correlation')
    (h,w) = img.shape[:2]
    for x in range(8):
        modihist.append(contrast[0][x]/10000)
    for x in range(8):
        modihist.append(energy[0][x]*10)
    for x in range(8):
        modihist.append(correlation[0][x])  
                      