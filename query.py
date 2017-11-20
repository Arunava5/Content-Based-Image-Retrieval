import cv2
from img_descriptors import img2modihist
from searcher import search
from tkinter import messagebox

def find_relevant(query_path,low,high,main):
    if query_path == '':
        messagebox.showinfo( "Error", "Please upload the query image before searching!")
        return []
    query_image = cv2.imread(query_path)
    query_seghist_features = img2modihist(query_image)

    retrieve_count = 10

    best_seghist = search(query_seghist_features,retrieve_count,low,high,main)
    return best_seghist
