import cv2

error_func = ( ("cv2.HISTCMP_HELLINGER",cv2.HISTCMP_HELLINGER),("cv2.HISTCMP_CORREL",cv2.HISTCMP_CORREL),
              ("cv2.HISTCMP_CHISQR",cv2.HISTCMP_CHISQR),("cv2.HISTCMP_INTERSECT",cv2.HISTCMP_INTERSECT) )
nobins = (2,4,8,16,32)

f = open("exp_results.txt","w")

for category in range(1,5):
    file_no = category*100 + 1
    filename = "Corel10K/" + str(file_no) + ".jpg"
    img_query = cv2.imread(filename)
    query_size = img_query.shape[0] * img_query.shape[1]
    img_query = cv2.cvtColor(img_query,cv2.COLOR_BGR2HSV)
    div_query = cv2.split(img_query)
    f.write("\n\nCategory: %d\n\n"%(category+1))
    print("Category: %d\n"%(category+1))
    for bins in nobins:
        f.write("\nBins : %d\n\n"%(bins))
        queryhist = []
#        queryhist = cv2.calcHist([img_query],[0,1,2],None,[bins,bins,bins],[0,180,0,256,0,256])
        queryhist.append(cv2.calcHist([div_query[0]],[0],None,[bins],[0,180]))
        queryhist.append(cv2.calcHist([div_query[1]],[0],None,[bins],[0,256]))
        queryhist.append(cv2.calcHist([div_query[2]],[0],None,[bins],[0,256]))
        for i in range(3):
            for k in range(bins):
                queryhist[i][k][0] *= 100
                queryhist[i][k][0] /= query_size
        for (name,method) in error_func:
            print("Bins : %d, Method: %s"%(bins,name))
            comparehists = []        
            for j in range(1,10001):
                if j%1000 == 0:
                    print(j)
                filename = "Corel10K/" + str(j) + ".jpg"
                img = cv2.imread(filename)
                img_size = img.shape[0] * img.shape[1]
                img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                div = cv2.split(img)
                hist = []
                hist.append(cv2.calcHist([div[0]],[0],None,[bins],[0,180]))
                hist.append(cv2.calcHist([div[1]],[0],None,[bins],[0,256]))
                hist.append(cv2.calcHist([div[2]],[0],None,[bins],[0,256]))
#                hist = cv2.calcHist([img],[0,1,2],None,[bins,bins,bins],[0,180,0,256,0,256])
#                val = cv2.compareHist(hist,queryhist,method)
                for i in range(3):
                    for k in range(bins):
                        hist[i][k][0] *= 100
                        hist[i][k][0] /= img_size
                val_blue = cv2.compareHist(queryhist[0],hist[0],method)
                val_green = cv2.compareHist(queryhist[1],hist[1],method)
                val_red = cv2.compareHist(queryhist[2],hist[2],method)
                comparehists.append((val_blue + val_green + val_red,j))
            
            if name == "cv2.HISTCMP_HELLINGER" or name == "cv2.HISTCMP_CHISQR":
                comparehists = sorted(comparehists)
            else:
                comparehists = sorted(comparehists,reverse = True)
            count = 0
            low = category*100 + 1
            high = category*100 + 100
            for i in range(25):
                if low <= comparehists[i][1] <= high :
                    count += 1
                    print("Image : %d"%(comparehists[i][1]))
            f.write("Method: %s, Accuracy: %d%%\n\n"%(name,count*4))

f.close()                