from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
created = ( "(1-5)","(6-10)","(11-15)","(16-20)" )

hell = []
corr = []
chisq = []
inter = []
cat = []

for category in created:
    filename = "exp_results" + category + ".txt"
    f = open(filename,"r")
    index = 0
    best_acc = [0,0,0,0]
    count = 0
    for line in f:
        if line[0] == "C":
            items = [ [] , [] , [] , [] ]
            best_acc[0] = best_acc[1] = best_acc[2] = best_acc[3] = -1
        if line[0] == "M":
            x = line.find("%")
            perc = int(line[x-1])
            if line[x-2] != " ":
                perc += 10 * int(line[x-2])
            best_acc[index] = max(best_acc[index],perc)
            items[index].append(perc)
            index = (index+1)%4
        if line[0] != "\n":
            count = count + 1
        if count == 41:
            hell.append(best_acc[0])
            corr.append(best_acc[1])
            chisq.append(best_acc[2])
            inter.append(best_acc[3])
            cat.append(items)
            count = 0
    f.close()

categories = [i for i in range(1,21)]
    
#print(hell)
#print(corr)
#print(chisq)
#print(inter)
#print(categories)        

plt.xlabel("Categories")
plt.ylabel("Precision")
plt.xlim(0,20)
plt.ylim(0,100)
plt.plot(categories,hell,color = "r")
plt.show()
plt.xlim(0,20)
plt.ylim(0,100)
plt.plot(categories,corr,color = "g")
plt.show()
plt.xlim(0,20)
plt.ylim(0,100)
plt.plot(categories,chisq,color = "b")
plt.show()
plt.xlim(0,20)
plt.ylim(0,100)
plt.plot(categories,inter,color = "c")
red_patch = mpatches.Patch(color="r", label="HELLINGER")
green_patch = mpatches.Patch(color="g", label="CORRELATION")
blue_patch = mpatches.Patch(color="b", label="CHI-SQUARE")
cyan_patch = mpatches.Patch(color="c", label="INTERSECT")
plt.legend(handles=[red_patch,green_patch,blue_patch,cyan_patch])
plt.show()

'''
#print(cat)
bins = [2,4,8,16,32,64,128,256]
plt.xlabel("Bins")
plt.ylabel("Precision")
for i in range(10,11):
    plt.title("Category: %d"%(i+1))
    plt.plot(bins,cat[i][0],color = "r")
    plt.plot(bins,cat[i][1],color = "g")
    plt.plot(bins,cat[i][2],color = "b")
    plt.plot(bins,cat[i][3],color = "c")   
    plt.xlim(0,256)
    plt.ylim(0,100)
    red_patch = mpatches.Patch(color="r", label="HELLINGER")
    green_patch = mpatches.Patch(color="g", label="CORRELATION")
    blue_patch = mpatches.Patch(color="b", label="CHI-SQUARE")
    cyan_patch = mpatches.Patch(color="c", label="INTERSECT")
    plt.legend(handles=[red_patch,green_patch,blue_patch,cyan_patch])
    plt.show()
'''
