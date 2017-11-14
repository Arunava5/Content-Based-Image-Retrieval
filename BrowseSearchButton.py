import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
#from minifeature_gen import gen_dataset
from tkinter import ttk
#for minifeature
import os
import cv2
from img_descriptors import img2modihist


main = tk.Tk()
main.geometry("900x900")
main.resizable()

frame1 = tk.Frame(main)
frame1.pack(padx = 20, pady = 20)
frame2 = tk.Frame(main)
frame2.pack()
frame3 = tk.Frame(main)
frame3.pack()
e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e1.insert(0,'1')
e2.insert(0,'1000')
e2.pack(side = 'bottom')
e1.pack(side = 'bottom')

label = tk.Label(frame1, image = None)
label1 = tk.Label(frame1, text = 'Content Based Image Retrieval')
label1.pack(fill = 'x', ipadx = 30, ipady = 30, padx = 30, pady = 30)
label1.config(fg = 'white', bg = 'black')
label2 = tk.Label()
Imagepath = ''
def chooseFile(type = 'public'):
      global Imagepath
      ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      Imagepath = ImageFile.name
      print(Imagepath)
      if ImageFile != None:
            data = Image.open(ImageFile)
            img = ImageTk.PhotoImage(data)
            #canvas = tk.Canvas(width=500,height=400)
            #canvas.create_image(0,0,image = img)
            #anvas.image = img
            #canvas.pack()
            label.config(image = img, bg = 'cyan')
            label.image = img
                 

      

button = tk.Button(frame1, text = 'Upload image', command = chooseFile)
button.pack()

label.pack(ipadx = 10, ipady = 10, padx = 5, pady = 5)



def search():
      
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()))
      for i in imgNum[:5]:
            #filenum = line
            filename = "C:/Users/Santanu PC/Desktop/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            #img = cv2.imread(filepath)
            #print(img)
            #cv2.imshow('image', img)
            #cv2.waitKey(0)
            label2 = tk.Label(frame2, image = None)
            label2.config(image = img, bg = 'red')
            label2.image = img
            label2.pack(side = 'left')
      for i in imgNum[5:10]:
            #filenum = line
            filename = "C:/Users/Santanu PC/Desktop/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            #img = cv2.imread(filepath)
            #print(img)
            #cv2.imshow('image', img)
            #cv2.waitKey(0)
            label2 = tk.Label(frame3, image = None)
            label2.config(image = img, bg = 'red')
            label2.image = img
            label2.pack(side = 'left')

def dataset():
      gen_dataset(int(e1.get()), int(e2.get()))
      
      
def clear_label():
      label2.config(image = '')
      label2.image = None
            
button1 = tk.Button(frame1, text = 'Search image', command = search)
button1.pack(side = 'left', padx = 20, pady = 20)

button2 = tk.Button(frame1, text = 'Generate dataset', command = dataset)
button2.pack(side = 'left', padx = 20, pady = 20)

button3 = tk.Button(frame1, text = 'Clear images', command = clear_label)
button3.pack(side = 'left', padx = 20, pady = 20)


progress=ttk.Progressbar(main,orient="horizontal",length=200, mode="determinate")

def prog(i,low,high):
	progress.pack()
	progress["maximum"]=high-low
	progress["value"]=i-low+1
	main.update()







#MINIFEATURE.PY


def gen_dataset(low,high):
	

    print("Creating Feature Vectors.....\n")

    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    os.mkdir(folder_name)

    file_seghist = open(folder_name+"/seghist.csv","w")

    high += 1
    step = (high - low)//10
	
	
    for i in range(low,high):
        if (i-low+1) % step == 0:
            print("%d%% complete\n"%((i-low+1)//step*10))
        filepath = "C:/Users/Santanu PC/Desktop/Corel10k/" + str(i) + ".jpg"
        image = cv2.imread(filepath)    
        modihist = img2modihist(image)
        modihist = [str(i) for i in modihist]    
        file_seghist.write("%s,%s\n"%(str(i),",".join(modihist)))
        prog(i,low,high)		   
    file_seghist.close()
	


	
	

    print("Feature Vectors created successfully!")








#STATUS BAR












main.mainloop()   