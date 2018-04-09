import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
from minifeature_gen import gen_dataset_retrieve
from feature_classify import gen_dataset_classify
from tkinter import messagebox
from classifier import classifyImage
from tkinter import font

categories = ['null','Painting','Bear','Wolf','Lion','Elephant','Tiger','Mountains','Swimming',
              'Historic Monuments','Vegetables','Woman','Dog','Clouds','Mushrooms','RandomPatterns(1)','Dinosaur',
              'Microbe','CycleAd','Sailboat','Barren Land','Atom','Oil Painting','Airfighter','Furniture',
              'Chimpanzee','WildSheeps and Antelopes','Millitary/Army','Waves','Cats','WaterAthletes',
              'RandomPatterns(2)','Microscopic World','Tree','Fish','RandomPatterns(3)','Floral Design','Lighthouse',
              'Bird','Stones n Crystals','RandomPatterns(4)','Polo','Spices','Candies','Flower Garden',
              'Horse','Musical Instrument','Flower','Leaf','Duck','Bird(2)','Sheet Designs','Beach Fashion',
              'Railway','RandomPatterns(5)']

labels = []
main = tk.Tk()
main.geometry("1400x900")
main.resizable()

helv36 = font.Font(family='Helvetica', size=12, weight='bold')

main.title("CONTENT BASED IMAGE RETRIEVAL-Final Year Project")
main.config(bg = '#292A33')
frame1 = tk.Frame(main)
frame1.pack(pady=10)
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
            label = tk.Label(frame1, image = None)
            label.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
            label.config(image = img, bg = '#18E5EA')
            label.image = img
            labels.append(label)                
button = tk.Button(frame1, text = 'UPLOAD IMAGE', command = chooseFile, font = helv36, padx=15,pady=4,bg ='#18E5EA',activebackground='#FC9F31', bd='5', relief='raised')
button.pack(pady = 10)


def search():
    
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()), main)
      if not imgNum:
          return
      for i in imgNum[:5]:
            filename = "C:/Mad/CBIR/Corel10k/"+str(i)+".jpg"
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
            filename = "C:/Mad/CBIR/Corel10k/"+str(i)+".jpg"
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
      global Imagepath
      Imagepath = ''
      for label in labels:
            label.destroy()

def gen_classify():
    gen_dataset_classify(int(e1.get()), int(e2.get()), main)
    
def classify():
    global Imagepath
    cnt = classifyImage(Imagepath,int(e1.get()), int(e2.get()))
    if cnt == 0:
        messagebox.showinfo('Error','Please select a query image to classify')
    elif cnt == -1:
        messagebox.showinfo('Error','No dataset found!')
    else:    
        messagebox.showinfo('Category','This image belongs to category: ' + categories[cnt])


button1 = tk.Button(frame2, text = 'GENERATE FEATURE VECTORS(RETRIEVAL)', font = helv36,command = dataset,padx=10,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button1.pack(side = 'left', padx = 10)
           
button2 = tk.Button(frame2, text = 'SEARCH  IMAGE', command = search,font = helv36,padx=10,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button2.pack(side = 'left', padx = 10)

button3 = tk.Button(frame2, text = 'GENERATE DATASET(CLASSIFICATION) ',font = helv36, command = gen_classify ,padx=10,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button3.pack(side = 'left', padx = 10)

button4 = tk.Button(frame2, text = 'CLASSIFY', font = helv36,command = classify,padx=10,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button4.pack(side = 'left', padx = 10)

button4 = tk.Button(frame2, text = 'CLEAR  IMAGES',font = helv36, command = clear_label,padx=10,pady=4,bg ='#18E5EA',activebackground='#18E5EA', bd='5', relief='raised')
button4.pack(side = 'left', padx = 10)

main.mainloop()   