import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
#from minifeature_gen import gen_dataset
from tkinter import ttk
import os
import cv2
from img_descriptors import img2modihist

labels = []
main = tk.Tk()
main.geometry("1200x900")
main.resizable()
main.title("Final Year Project")
main.config(bg = 'black')
frame1 = tk.Frame(main)
frame1.pack()
frame1.config(bg = 'black')
frame2 = tk.Frame(main)
frame2.pack(padx = 5, pady = 5)
frame2.config(bg = 'black')
frame3 = tk.Frame(main)
frame3.config(bg = 'black')
frame3.pack(padx = 5, pady = 5)
e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e1.insert(0,'1')
e2.insert(0,'1000')
e2.pack(side = 'bottom')
e1.pack(side = 'bottom')

label = tk.Label(frame1, image = None)
label1 = tk.Label(frame1, text = 'Content Based Image Retrieval')
label1.pack(ipadx = 20, ipady = 10, padx = 10, pady = 10)
label1.config(font = ('Algerian', 20), fg = 'white', bg = 'black')



Imagepath = ''
def chooseFile(type = 'public'):
      global Imagepath
      ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      Imagepath = ImageFile.name
      print(Imagepath)
      if ImageFile != None:
            data = Image.open(ImageFile)
            img = ImageTk.PhotoImage(data)
            label.config(image = img, bg = 'red')
            label.image = img
                

button = tk.Button(frame1, text = 'Upload image', command = chooseFile)
button.pack()

label.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
label.update
def search():
      
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()))
      
      for i in imgNum[:5]:
            filename = "C:/Users/Arunava/MycvProjects/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            label2 = tk.Label(frame2, image = None)
            labels.append(label2)
            label2.config(image = img, bg = 'blue')
            label2.image = img
            label2.pack(side = 'left', ipadx = 3, ipady = 3, padx = 10, pady = 5)
      for i in imgNum[5:10]:
            filename = "C:/Users/Arunava/MycvProjects/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            label3 = tk.Label(frame3, image = None)
            labels.append(label3)
            label3.config(image = img, bg = 'blue')
            label3.image = img
            label3.pack(side = 'left',  ipadx = 3, ipady = 3, padx = 10, pady = 5)
      
      
def gen_dataset(low, high):
	

    print("Creating Feature Vectors.....\n")

    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    os.mkdir(folder_name)

    file_seghist = open(folder_name+"/seghist.csv","w")

    high += 1
    step = (high - low)//10
	
	
    for i in range(low,high):
        if (i-low+1) % step == 0:
            print("%d%% complete\n"%((i-low+1)//step*10))
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(i) + ".jpg"
        image = cv2.imread(filepath)    
        modihist = img2modihist(image)
        modihist = [str(i) for i in modihist]    
        file_seghist.write("%s,%s\n"%(str(i),",".join(modihist)))
        prog(i,low,high)		   
    file_seghist.close()
    print("Feature Vectors created successfully!")


def dataset():
      gen_dataset(int(e1.get()), int(e2.get()))      
      
def clear_label():
      for label in labels:
            label.destroy()
            
button1 = tk.Button(frame1, text = 'Search image', command = search)
button1.pack(side = 'left', padx = 40, pady = 10)

button2 = tk.Button(frame1, text = 'Generate dataset', command = dataset)
button2.pack(side = 'left', padx = 40, pady = 10)

button3 = tk.Button(frame1, text = 'Clear images', command = clear_label)
button3.pack(side = 'left', padx = 10, pady = 10)




progress=ttk.Progressbar(main,orient="horizontal",length=200, mode="determinate")

def prog(i,low,high):
	progress.pack()
	progress["maximum"]=high-low
	progress["value"]=i-low+1
	main.update()

main.mainloop()   