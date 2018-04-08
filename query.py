import cv2
import numpy as np
from img_descriptors import img2modihist,w2d
from skimage.feature import greycomatrix as gc
from skimage.feature import greycoprops as gp
from searcher import search
from tkinter import messagebox

def find_relevant(query_path,low,high,main):
    if query_path == '':
        messagebox.showinfo( "Error", "Please upload the query image before searching!")
        return []
    query_image = cv2.imread(query_path)
    query_seghist_features = img2modihist(query_image)
    img = w2d(query_path,'db1',5)
    grey = gc(img,[1],[0, np.pi/4, np.pi/2, 3*np.pi/4],levels = 256)
    contrast = gp(grey,'contrast')
    energy = gp(grey,'energy')
    (h,w) = img.shape[:2]
    tot = h*w
    for x in range(4):
        query_seghist_features.append(contrast[0][x]/(tot*10000))
    for x in range(4):
        query_seghist_features.append(energy[0][x]/tot)


    retrieve_count = 10

    best_seghist = search(query_seghist_features,retrieve_count,low,high,main)
    return best_seghist
