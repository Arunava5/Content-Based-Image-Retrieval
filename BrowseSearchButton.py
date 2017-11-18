import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
#from minifeature_gen import gen_dataset
from tkinter import ttk
import os
import cv2
from img_descriptors import img2modihist
from tkinter import messagebox



labels = []
main = tk.Tk()
main.geometry("1200x900")
main.resizable()

main.title("CONTENT BASED IMAGE RETRIEVAL-Final Year Project")
main.config(bg = '#292A33')
frame1 = tk.Frame(main)
frame1.pack()
frame1.config(bg = '#292A33')
frame2 = tk.Frame(main)
frame2.pack(padx = 5, pady = 5)
frame2.config(bg = '#292A33')
frame3 = tk.Frame(main)
frame3.config(bg = '#292A33')
frame3.pack(padx = 5, pady = 5)




e1 = tk.Entry(frame1,bg='#292A33',fg='white')
e2 = tk.Entry(frame1,bg='#292A33',fg='white')
e1.insert(0,'1')
e2.insert(0,'1000')
e2.pack(side = 'bottom')
e1.pack(side = 'bottom',pady=5)

label = tk.Label(frame1, image = None)
label1 = tk.Label(frame1, text = 'Content Based Image Retrieval System')
label1.pack(ipadx = 20, ipady = 10, padx = 10, pady = 40)
label1.config(font = ('algerian', 30), fg = '#18E5EA', bg = '#292A33')



Imagepath = ''
def chooseFile(type = 'public'):
      global Imagepath
      ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      Imagepath = ImageFile.name
      print(Imagepath)
      if ImageFile != None:
            data = Image.open(ImageFile)
            img = ImageTk.PhotoImage(data)
            label.config(image = img, bg = '#18E5EA')
            label.image = img
                

button = tk.Button(frame1, text = 'UPLOAD IMAGE', command = chooseFile, padx=15,pady=5,bg ='#18E5EA',activebackground='#FC9F31', bd='5', relief='raised')
button.pack()

label.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
label.update
def search():
      
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()))
      
      for i in imgNum[:5]:
            filename = "C:/Users/Santanu PC/Desktop/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            label2 = tk.Label(frame2, image = None)
            labels.append(label2)
            label2.config(image = img, bg = '#FC9F31')
            label2.image = img
            label2.pack(side = 'left', ipadx = 3, ipady = 1, padx = 10, pady = 1)
      for i in imgNum[5:10]:
            filename = "C:/Users/Santanu PC/Desktop/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            img = ImageTk.PhotoImage(data)
            label3 = tk.Label(frame3, image = None)
            labels.append(label3)
            label3.config(image = img, bg = '#FC9F31')
            label3.image = img
            label3.pack(side = 'left',  ipadx = 3, ipady = 1, padx = 10, pady = 1)




     
def gen_dataset(low, high):
	

    print("Creating Feature Vectors.....\n")

    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    os.mkdir(folder_name)

    file_seghist = open(folder_name+"/seghist.csv","w")

    high += 1
    step = (high - low)//10
	
    popup = tk.Toplevel()
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - 150
    y = (screen_height/2) - 50
    popup.geometry("300x100+%d+%d"%(x,y))
    popup.title("Generating Dataset")	
    tk.Label(popup).grid(row=0,column=0)
    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, length = 300,maximum=high-low)
    progress_bar.grid(row=1, column=0)
    popup.pack_slaves()
    for i in range(low,high):
        if (i-low+1) % step == 0:
            print("%d%% complete\n"%((i-low+1)//step*10))
        filepath = "C:/Users/Santanu PC/Desktop/Corel10k/" + str(i) + ".jpg"
        image = cv2.imread(filepath)    
        modihist = img2modihist(image)
        modihist = [str(i) for i in modihist]    
        file_seghist.write("%s,%s\n"%(str(i),",".join(modihist)))
        popup.update()
        progress += 1
        progress_var.set(progress)
#        prog(i,low,high)		   
    file_seghist.close()
    popup.destroy()
#    label4 = tk.Label(frame2,text = "Dataset has been generated",padx = 5,pady = 5)
#    label4.config(font = ('Impact',14),fg = '#18E5EA',bg = '#292A33')
#    label4.pack(side = 'top')
    messagebox.showinfo( "Feature vector Generation", "Feature vectors Generated")
    print("Feature Vectors created successfully!")


def dataset():
      gen_dataset(int(e1.get()), int(e2.get()))      
      
def clear_label():
      for label in labels:
            label.destroy()
            
button1 = tk.Button(frame1, text = 'SEARCH  IMAGE', command = search,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button1.pack(side = 'left', padx = 75)

button2 = tk.Button(frame1, text = 'GENERATE  FEATURE  VECTORS', command = dataset,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button2.pack(side = 'left', padx = 40)

button3 = tk.Button(frame1, text = 'CLEAR  IMAGES', command = clear_label,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button3.pack(side = 'left', padx = 60)




'''
progress=ttk.Progressbar(main,orient="horizontal",length=200, mode="determinate")

def prog(i,low,high):
	progress.pack()
	progress["maximum"]=high-low
	progress["value"]=i-low+1
	main.update()
'''
main.mainloop()   