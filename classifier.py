import os
import numpy as np
from six.moves import cPickle as pickle
import cv2
from img_descriptors import img2modihist,w2d,texcal
from sklearn.linear_model import LogisticRegression

def classifyImage(queryPath,low,high):
    
    if queryPath == '':
        return 0
    set_filename = 'DataSet(' + str(low) + '-' + str(high) + ').pickle'
    if not os.path.exists(set_filename):
        return -1
            
    with open(set_filename, 'rb') as f:
        dataset = pickle.load(f)
    
    fvector_size = 11 * 8 * 9 * 5 + 24

    train_size = dataset[4]
    test_size = dataset[5]
    
    train_dataset = np.ndarray(shape=(train_size,fvector_size),dtype=np.float32)  
    test_dataset  = np.ndarray(shape=(test_size,fvector_size),dtype=np.float32)
    train_labels = np.ndarray(train_size,dtype=np.int32)
    test_labels = np.ndarray(test_size,dtype=np.int32)    
      
    train_dataset = dataset[0]
    train_labels = dataset[1]
    test_dataset = dataset[2]
    test_labels = dataset[3]

    
    image = cv2.imread(queryPath)
    
    modihist = img2modihist(image)
        
    img = w2d(queryPath,'db1',5)
      
    texcal(img,modihist)
    
    query_dataset = np.ndarray(shape = (1,fvector_size),dtype=np.float32)
    query_dataset[0] = modihist
        
        
    clf = LogisticRegression()
    clf.fit(train_dataset, train_labels)
        
    return(clf.predict(query_dataset)[0])
   
   

