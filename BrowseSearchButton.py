import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
from minifeature_gen import gen_dataset_retrieve
from checkAccuracy import gen_dataset_classify
from tkinter import messagebox

categories = ['null','Painting','Bear','Wolf','Lion','Elephant','Tiger','Mountains','Swimming',
              'Historic Monuments','Vegetables','Woman','Dog','Clouds','Mushrooms']
labels = []
main = tk.Tk()
main.geometry("1400x900")
main.resizable()

main.title("CONTENT BASED IMAGE RETRIEVAL-Final Year Project")
main.config(bg = '#292A33')
frame1 = tk.Frame(main)
frame1.pack()
frame1.config(bg = '#292A33')
frame2 = tk.Frame(main)
frame2.pack()
frame2.config(bg = '#292A33')
frame3 = tk.Frame(main)
frame3.pack(padx = 5, pady = 5)
frame3.config(bg = '#292A33')
frame4 = tk.Frame(main)
frame4.pack(padx = 5, pady = 5)
frame4.config(bg = '#292A33')

e1 = tk.Entry(frame2,bg='#292A33',fg='white')
e2 = tk.Entry(frame2,bg='#292A33',fg='white')
e1.insert(0,'1')
e2.insert(0,'500')
e2.pack(side = 'bottom')
e1.pack(side = 'bottom',pady=5)

label1 = tk.Label(frame1, text = 'Content Based Image Retrieval System')
label1.pack(ipadx = 0, ipady = 20, padx = 0, pady = 0)
label1.config(font = ('algerian', 30), fg = '#18E5EA', bg = '#292A33')

Imagepath = ''
label = tk.Label(frame1, image = None)

def chooseFile(type = 'public'):
      global Imagepath
      ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      if ImageFile != None:
            Imagepath = ImageFile.name
            data = Image.open(ImageFile)
            (w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)
            img = ImageTk.PhotoImage(data)
            label.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
            label.config(image = img, bg = '#18E5EA')
            label.image = img
                            
button = tk.Button(frame1, text = 'UPLOAD IMAGE', command = chooseFile, padx=15,pady=4,bg ='#18E5EA',activebackground='#FC9F31', bd='5', relief='raised')
button.pack(pady = 10)


def search():
    
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()), main)
      if not imgNum:
          return
      for i in imgNum[:5]:
            filename = "C:/Users/Arunava/MycvProjects/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            (w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)
            img = ImageTk.PhotoImage(data)
            label2 = tk.Label(frame3, image = None)
            labels.append(label2)
            label2.config(image = img, bg = '#FC9F31')
            label2.image = img
            label2.pack(side = 'left', ipadx = 3, ipady = 1, padx = 10, pady = 1)

      for i in imgNum[5:10]:
            filename = "C:/Users/Arunava/MycvProjects/Corel10k/"+str(i)+".jpg"
            data = Image.open(filename)
            (w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)
            img = ImageTk.PhotoImage(data)
            label3 = tk.Label(frame4, image = None)
            labels.append(label3)
            label3.config(image = img, bg = '#FC9F31')
            label3.image = img
            label3.pack(side = 'left',  ipadx = 3, ipady = 1, padx = 10, pady = 3)

def dataset():
      gen_dataset_retrieve(int(e1.get()), int(e2.get()), main)      
      
def clear_label():
      for label in labels:
            label.destroy()

def classify():
    cat = gen_dataset_classify(int(e1.get()), int(e2.get()), Imagepath, main )
    if cat != 0:
        messagebox.showinfo('Category','This image belongs to Category: ' + categories[cat])
           
button1 = tk.Button(frame2, text = 'SEARCH  IMAGE', command = search,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button1.pack(side = 'left', padx = 50)

button2 = tk.Button(frame2, text = 'GENERATE  FEATURE VECTORS', command = dataset,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button2.pack(side = 'left', padx = 50)

button3 = tk.Button(frame2, text = 'CLASSIFY', command = classify,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button3.pack(side = 'left', padx = 50)

button4 = tk.Button(frame2, text = 'CLEAR  IMAGES', command = clear_label,padx=20,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button4.pack(side = 'left', padx = 50)

main.mainloop()   