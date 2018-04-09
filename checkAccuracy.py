from __future__ import print_function
import cv2
import numpy as np
from sklearn.linear_model import LogisticRegression
from six.moves import range
from img_descriptors import img2modihist,w2d,texcal
import math
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from six.moves import cPickle as pickle
import os

def gen_dataset_classify(low,high,queryPath,main):
    
    set_filename = 'DataSet(' + str(low) + '-' + str(high) + ')'
    
    fvector_size = 11 * 8 * 9 * 5 + 24
    query_dataset = np.ndarray(shape=(1,fvector_size),dtype=np.float32)

    isok = True
    if os.path.exists(set_filename):
        result = messagebox.askquestion('Alert','Dataset already exists. Replace?',icon='warning')
        if result == 'no':
            isok = False
            
    if isok == False:
        with open(set_filename, 'rb') as f:
            dataset = pickle.load(f)
      
        train_dataset = dataset[0]
        train_labels = dataset[1]
        test_dataset = dataset[2]
        test_labels = dataset[3]
        
        if queryPath == '':
            return 0
        
        image = cv2.imread(queryPath)
    
        modihist = img2modihist(image)
        
        img = w2d(queryPath,'db1',5)
      
        texcal(img,modihist)
        
        query_dataset[0] = modihist
        
        
        clf = LogisticRegression()
        clf.fit(train_dataset, train_labels)
        
        return(clf.predict(query_dataset)[0])
    
    train_images = []
    test_images = []
    
    templow = low
    temphigh = high    
    
    if low%100 != 1:
        images = []
        while low%100 != 1:
            images.append(low)
            low += 1
        tot = len(images)
        permutation = np.random.permutation(images)
        reqd = math.ceil(0.9*tot)
        for k in range(reqd):
            train_images.append(permutation[k])
        for k in range(reqd,tot):
            test_images.append(permutation[k])
            
    if high%100 != 0:
        images = []
        while high%100 != 0:
            images.append(high)
            high -= 1
        tot = len(images)
        permutation = np.random.permutation(images)
        reqd = math.ceil(0.9*tot)
        for k in range(reqd):
            train_images.append(permutation[k])
        for k in range(reqd,tot):
            test_images.append(permutation[k])
           
    while low < high:
        permutation = np.random.permutation(100)
        
        for k in range(90):
            train_images.append(permutation[k]+low)
        for k in range(90,100):
            test_images.append(permutation[k]+low) 
        low += 100    
    
    traindex = 0
    testdex = 0 
   
    train_size = len(train_images)
    test_size = len(test_images)   
    train_dataset = np.ndarray(shape=(train_size,fvector_size),dtype=np.float32)  
    test_dataset  = np.ndarray(shape=(test_size,fvector_size),dtype=np.float32)
    train_labels = np.ndarray(train_size,dtype=np.int32)
    test_labels = np.ndarray(test_size,dtype=np.int32)
    
    popup = tk.Toplevel()
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    x = (screen_width/2) - 150
    y = (screen_height/2) - 50
    popup.geometry("400x100+%d+%d"%(x,y))
    popup.title("Generating Training & Testing Datasets")	
    tk.Label(popup).grid(row=0,column=0)
    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, length = 400,maximum=temphigh-templow+1)
    progress_bar.grid(row=1, column=0)
    popup.pack_slaves()
    
    for m in train_images:
      
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(m) + ".jpg"
        image = cv2.imread(filepath)
 
        modihist = img2modihist(image)
        
        img = w2d(filepath,'db1',5)
        
        texcal(img,modihist)
        
        train_dataset[traindex:] = modihist
        train_labels[traindex] = (m-1)//100 + 1
        traindex += 1
        
        popup.update()
        progress += 1
        progress_var.set(progress)
    
    for m in test_images:
         
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(m) + ".jpg"
        image = cv2.imread(filepath)
    
        modihist = img2modihist(image)
        
        img = w2d(filepath,'db1',5)
        
        texcal(img,modihist)
 
        test_dataset[testdex:] = modihist
        test_labels[testdex] = (m-1)//100 + 1
        testdex += 1
        
        popup.update()
        progress += 1
        progress_var.set(progress)
    
    print(test_images)    
    popup.destroy()
    messagebox.showinfo( "Dataset Creation", "Datasets have been successfully generated!")         
    
    dataset = []
    dataset.append(train_dataset)
    dataset.append(train_labels)
    dataset.append(test_dataset)
    dataset.append(test_labels)
                       
    with open(set_filename, 'wb') as f:
          pickle.dump(dataset, f, pickle.HIGHEST_PROTOCOL)        
        
    
    if queryPath == '':
        return 0        
    image = cv2.imread(queryPath)
    
    modihist = img2modihist(image)
        
    img = w2d(queryPath,'db1',5)
      
    texcal(img,modihist)
        
    query_dataset[0] = modihist
        
    clf = LogisticRegression()
    clf.fit(train_dataset, train_labels)       
    return(clf.predict(query_dataset)[0])
   
