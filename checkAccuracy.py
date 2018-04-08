# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:59:02 2018

@author: Arunava
"""

from __future__ import print_function
import cv2
import numpy as np
from sklearn.linear_model import LogisticRegression
from six.moves import range
from img_descriptors import img2modihist,w2d
from skimage.feature import greycomatrix as gc
from skimage.feature import greycoprops as gp

def gen_dataset(low,high):

    high += 1
    traindex = 0
    testdex = 0 
    for m in range(low,high):
        if m%100 == 0:
            print(m)
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(m) + ".jpg"

        image = cv2.imread(filepath)
    
        image = cv2.imread(filepath)
    
        modihist = img2modihist(image)
        
        img = w2d(filepath,'db1',5)
        grey = gc(img,[1],[0, np.pi/4, np.pi/2, 3*np.pi/4],levels = 256)
        contrast = gp(grey,'contrast')
        energy = gp(grey,'energy')
        (h,w) = img.shape[:2]
        tot = h*w
        for x in range(4):
            modihist.append(contrast[0][x]/(tot*10000))
        for x in range(4):
            modihist.append(energy[0][x]/tot)
           
        
        if (m-1)%100 >= 90:
            test_dataset[testdex:] = modihist
            test_labels[testdex] = (m-1)//100
            testdex += 1
        else:
            train_dataset[traindex:] = modihist
            train_labels[traindex] = (m-1)//100
            traindex += 1
            
low = 1
high = 10000
tot = high - low + 1
train_size = int(0.9*tot)
test_size = int(0.1*tot)
num_labels = tot//100

def randomize(dataset, labels):
  permutation = np.random.permutation(labels.shape[0])
  shuffled_dataset = dataset[permutation,:]
  shuffled_labels = labels[permutation]
  return shuffled_dataset, shuffled_labels

fvector_size = 11 * 8 * 9 * 5 + 8
train_dataset = np.ndarray(shape=(train_size,fvector_size),dtype=np.float32)  
test_dataset  = np.ndarray(shape=(test_size,fvector_size),dtype=np.float32)
train_labels = np.ndarray(train_size,dtype=np.int32)
test_labels = np.ndarray(test_size,dtype=np.int32)
gen_dataset(low,high)

train_dataset, train_labels = randomize(train_dataset, train_labels)
test_dataset, test_labels = randomize(test_dataset, test_labels)

clf = LogisticRegression()
#f.write("Bins: %d %d %d\nLogisticRegression score: %f\n\n"%(binh,binsa,binv,clf.fit(train_dataset, train_labels).score(test_dataset, test_labels)))
print("LogisticRegression score: %f\n"% clf.fit(train_dataset, train_labels).score(test_dataset, test_labels))


'''
f = open("NewOutputfile2.txt","w")

def reformat(dataset, labels):
  dataset = dataset.reshape((-1, fvector_size)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
  return dataset, labels

def accuracy(predictions, labels):
  return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))
          / predictions.shape[0])
  
for binh in range(11,12):
    for binsa in range(8,9):
        for binv in range(9,10):
            print(binh,binsa,binv)
            fvector_size = binh * binsa * binv * 5
            train_dataset = np.ndarray(shape=(train_size,fvector_size),dtype=np.float32)  
            test_dataset  = np.ndarray(shape=(test_size,fvector_size),dtype=np.float32)
            train_labels = np.ndarray(train_size,dtype=np.int32)
            test_labels = np.ndarray(test_size,dtype=np.int32)
            bins = (binh,binsa,binv)
            gen_dataset(low,high)
            train_dataset, train_labels = randomize(train_dataset, train_labels)
            test_dataset, test_labels = randomize(test_dataset, test_labels)
            train_dataset, train_labels = reformat(train_dataset, train_labels)
            test_dataset, test_labels = reformat(test_dataset, test_labels)
            train_subset = tot

            graph = tf.Graph()
            with graph.as_default():

                # Input data.
                # Load the training, validation and test data into constants that are
                # attached to the graph.
                tf_train_dataset = tf.constant(train_dataset[:train_subset, :])
                tf_train_labels = tf.constant(train_labels[:train_subset])
                tf_test_dataset = tf.constant(test_dataset)
  
  # Variables.
  # These are the parameters that we are going to be training. The weight
  # matrix will be initialized using random values following a (truncated)
  # normal distribution. The biases get initialized to zero.
                weights = tf.Variable(
                tf.truncated_normal([fvector_size, num_labels]))
                biases = tf.Variable(tf.zeros([num_labels]))
  
  # Training computation.
  # We multiply the inputs with the weight matrix, and add biases. We compute
  # the softmax and cross-entropy (it's one operation in TensorFlow, because
  # it's very common, and it can be optimized). We take the average of this
  # cross-entropy across all training examples: that's our loss.
                logits = tf.matmul(tf_train_dataset, weights) + biases
                loss = tf.reduce_mean(
                tf.nn.softmax_cross_entropy_with_logits(labels=tf_train_labels, logits=logits))
  
  # Optimizer.
  # We are going to find the minimum of this loss using gradient descent.
                optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
  
  # Predictions for the training, validation, and test data.
  # These are not part of training, but merely here so that we can report
  # accuracy figures as we train.
                train_prediction = tf.nn.softmax(logits)
                test_prediction = tf.nn.softmax(tf.matmul(tf_test_dataset, weights) + biases)
  
                num_steps = 5000



            with tf.Session(graph=graph) as session:
  # This is a one-time operation which ensures the parameters get initialized as
  # we described in the graph: random weights for the matrix, zeros for the
  # biases. 
                tf.global_variables_initializer().run()
#                print('Initialized')
                for step in range(num_steps):
    # Run the computations. We tell .run() that we want to run the optimizer,
    # and get the loss value and the training predictions returned as numpy
    # arrays.
                    _, l, predictions = session.run([optimizer, loss, train_prediction])
                    if (step % 100 == 0):
                        print('Loss at step %d: %f' % (step, l))
                        print('Training accuracy: %.1f%%' % accuracy(predictions, train_labels[:train_subset, :]))
      # Calling .eval() on valid_prediction is basically like calling run(), but
      # just to get that one numpy array. Note that it recomputes all its graph
      # dependencies.

                        print('Test accuracy: %.1f%%' % accuracy(test_prediction.eval(), test_labels))            
'''            

'''
f.close()
#with open(train_pickle_file, "wb") as f:
#    pickle.dump(train_dataset, f, pickle.HIGHEST_PROTOCOL)
#with open(test_pickle_file, "wb") as f:
#    pickle.dump(test_dataset, f, pickle.HIGHEST_PROTOCOL)

print(train_dataset.shape)
print(np.mean(train_dataset))
print(np.std(train_dataset))
print(test_dataset.shape)
print(np.mean(test_dataset))
print(np.std(test_dataset))

print('Training:', train_dataset.shape, train_labels.shape)
print('Testing:', test_dataset.shape, test_labels.shape)




print('Training set', train_dataset.shape, train_labels.shape)
print('Test set', test_dataset.shape, test_labels.shape)
'''
# With gradient descent training, even this much data is prohibitive.
# Subset the training data for faster turnaround. 