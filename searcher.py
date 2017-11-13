import csv
from scipy.spatial import distance as dist

def search(query_features,limit,low,high,mode):
    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    results = {}
    total = high - low + 1
    if mode == 0:
        featureset_path = folder_name + "/hist.csv"
    else:
        featureset_path = folder_name + "/seghist.csv"
        
    with open(featureset_path) as file:
        reader = csv.reader(file)
        count = 0
        step = total//10
        for row in reader:
            count +=1 
            if count % step == 0:
                print("%d%% complete\n"%(count//step*10))
            features = [float(x) for x in row[1:]]
            d = dist.euclidean(features,query_features)
            results[row[0]] = d
            
    file.close()
    results = sorted([(v,k) for (k,v) in results.items()])
    return [x[1] for x in results[:limit]]        