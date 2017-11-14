import cv2
from img_descriptors import img2modihist
from searcher import search

def find_relevant(query_path,low,high):
    
    query_image = cv2.imread(query_path)

    query_seghist_features = img2modihist(query_image)

    retrieve_count = 10

    print("Searching for relevant images.....\n")

    best_seghist = search(query_seghist_features,retrieve_count,low,high,1)

    print(best_seghist)
    return best_seghist
