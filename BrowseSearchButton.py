import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
from query import find_relevant
from minifeature_gen import gen_dataset_retrieve
from feature_classify import gen_dataset_classify
from tkinter import messagebox
from classifier import classifyImage
from tkinter import font
from loc_dataset import location

categories = ['null','Painting','Bear','Wolf','Lion','Elephant','Tiger','Mountains','Swimming',
              'Historic Monuments','Vegetables','Woman','Dog','Clouds','Mushrooms','Fort','Kid\'s Poster',
              'Tribal People','Juice','Martial Arts','Universe','Books','Fruits','Tree Sampling',
              'Sign Boards','Crackers','House Door','Deer','Racing Cars','Bridges','Water Body',
              'Land Patches','House Interior','Sea-shells','Road Signs','Beaches','Stone Pellets',
              'Sunset','Car','Graphic Art','Playing Cards','Rhinoceros','Butterfly','Ceramics',
              'Dolls','Tools','Houses','Guns','National Flags','Coal Train','Kaleidoscope Visualisations',
              'Tennis','Stamps','Air Baloons','Medicine Pellets','Ships','Pastries','Buses','Oil Paintings',
              'Coloured Eggs','Bikes','Beads','Dinosaur',
              'Microbe','CycleAd','Sailboat','Barren Land','Atom','Oil Painting','Airfighter','Furniture',
              'Chimpanzee','WildSheeps and Antelopes','Millitary/Army','Waves','Cats','WaterAthletes',
              'Underwater Designs','Microscopic World','Tree','Fish','Wooden Designs','Floral Design','Lighthouse',
              'Bird','Stones n Crystals','Crystal Art','Polo','Spices','Candies','Flower Garden',
              'Horse','Musical Instrument','Flower','Leaf','Duck','Bird(2)','Sheet Designs','Beach Fashion',
              'Railway','Ferns']


main = tk.Tk()
main.geometry("1400x900")
main.resizable()

helv36 = font.Font(family='Helvetica', size=12, weight='bold')
helv37 = font.Font(family='Helvetica', size=15, weight = 'bold')

main.title("CONTENT BASED IMAGE RETRIEVAL - Final Year Project(14UP04)")
main.config(bg = '#292A33')#GREY COLOR
#main.config(bg='#FFFFFF')
frame1 = tk.Frame(main)
frame1.pack(pady=10)
frame1.config(bg = '#292A33')
frame2 = tk.Frame(main)
frame2.pack()
frame2.config(bg = '#292A33')
frame3 = tk.Frame(main)
frame3.pack(padx = 5, pady = 5)
frame3.config(bg = '#292A33')
#frame4 = tk.Frame(main)
#frame4.pack(padx = 5, pady = 5)
#frame4.config(bg = '#FFFFFF')
			  
			  
label3 = tk.Label(frame2, text = 'ENTER RANGE:')
label3.pack(ipadx = 0, ipady = 0, padx = 0, pady = 0)
label3.config(font = ('ariel', 18), fg = 'white', bg = '#292A33')		  
			  

e1 = tk.Entry(frame2,bg='#FFFFFF',fg='black',font = helv37)
e2 = tk.Entry(frame2,bg='#FFFFFF',fg='black',font = helv37)
e1.insert(0,'1')

#DASH
label3 = tk.Label(frame2, text = '--')

label3.config(bg = '#292A33', fg= 'white')
labels = []



e2.insert(0,'500')
e2.pack(side = 'right',ipadx=10,ipady=10,padx = 10)
label3.pack(ipadx = 0, ipady = 0, padx = 0, pady = 0,side='right')
e1.pack(side = 'right',ipadx=10,ipady=10,pady=10, padx = 10)

label1 = tk.Label(frame1, text = 'Content Based Image Retrieval System')
label1.pack(ipadx = 0, ipady = 20, padx = 0, pady = 0)
label1.config(font = ('algerian', 30), fg = 'white', bg = '#292A33')

			  
			  
  
			  
Imagepath = ''
def chooseFile(type = 'public'):
      global data
      global Imagepath
      if Imagepath != '':
          clear_label()
          Imagepath = ''
      ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      if ImageFile != None:
            Imagepath = ImageFile.name
            data = Image.open(ImageFile)
            '''(w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)'''
            img = ImageTk.PhotoImage(data)
            label = tk.Label(frame1, image = None)
            label.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
            label.config(image = img, bg = 'black')
            label.image = img
            labels.append(label)                
button = tk.Button(frame1, text = 'UPLOAD  IMAGE', command = chooseFile, font = helv36, padx=15,pady=4,foreground = 'black',bg ='#ffffff',activebackground='black', bd='2', relief='raised')
button.pack(pady = 10)


def search():
      global data 
      imgNum = find_relevant(Imagepath, int(e1.get()), int(e2.get()), main)
      new = tk.Toplevel()
      new.geometry("1400x900")
      new.resizable()
      newFrame1 = tk.Frame(new)
      newFrame1.pack(pady = 10)
      newFrame2 = tk.Frame(new)
      newFrame2.pack(pady = 10)
      newFrame3 = tk.Frame(new)
      newFrame3.pack(pady = 10)
      
      newLabel1 = tk.Label(newFrame1, text = 'Query Image:', font = helv37)
      newLabel1.pack(side = 'top')
      newLabel2 = tk.Label(newFrame2, text = 'Search Results:', font = helv37)
      newLabel2.pack(side = 'top')
      
      queryimg = ImageTk.PhotoImage(data)
      queryLabel = tk.Label(newFrame1, image = None)
      queryLabel.pack(ipadx = 3, ipady = 3, padx = 5, pady = 5)
      queryLabel.config(image = queryimg, bg = 'black')
      queryLabel.image = queryimg
      
     
      if not imgNum:
          return
      for i in imgNum[:5]:
            filename = location + str(i) + ".jpg"
            data = Image.open(filename)
            '''(w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)'''
            img = ImageTk.PhotoImage(data)
            label2 = tk.Label(newFrame2, image = None)
            label2.config(image = img, bg = '#FC9F31')
            label2.pack(side = 'left', ipadx = 3, ipady = 1, padx = 10, pady = 1)
            label2.image = img
      for i in imgNum[5:10]:
            filename = location + str(i) + ".jpg"
            data = Image.open(filename)
            '''(w,h) = data.size
            if h > 130:
                r = 130 / h
                dim = (int(r*w),130)
                data.thumbnail(dim, Image.ANTIALIAS)'''
            img = ImageTk.PhotoImage(data)
            label3 = tk.Label(newFrame3, image = None)
            label3.config(image = img, bg = '#FC9F31')
            label3.pack(side = 'left',  ipadx = 3, ipady = 1, padx = 10, pady = 3)
            label3.image = img

def dataset():
      gen_dataset_retrieve(int(e1.get()), int(e2.get()), main)      
      

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

def clear_label():
      for label in labels:
            label.destroy()
      

def OpenStartPage():
      main.destroy()
      exec(compile(open("Welcome.py").read(), "Welcome.py", 'exec'))
      #import Welcome

button1 = tk.Button(frame3, text = 'GENERATE  FEATURE  VECTORS  (RETRIEVAL)', foreground = 'black',font = helv36,command = dataset,padx=10,pady=4,bg ='white',activebackground='white', bd='2', relief='raised')
button1.pack(side = 'top', padx = 10, pady = 15)
           
button2 = tk.Button(frame3, text = 'SEARCH  IMAGE', command = search,font = helv36,padx=10,pady=4,bg ='white', foreground = 'black',activebackground='white', bd='2', relief='raised')
button2.pack(side = 'top', padx = 10, pady = 15)

button3 = tk.Button(frame3, text = 'GENERATE  DATASET  (CLASSIFICATION) ',font = helv36, foreground = 'black', command = gen_classify ,padx=10,pady=4,bg ='white',activebackground='white', bd='2', relief='raised')
button3.pack(side = 'top', padx = 10, pady = 15)

button4 = tk.Button(frame3, text = 'CLASSIFY', font = helv36,command = classify,padx=10,pady=4, foreground = 'black',bg ='white',activebackground='white', bd='2', relief='raised')
button4.pack(side = 'top', padx = 10, pady = 15)

button5 = tk.Button(frame3, text = '<Back',font = helv36, command = OpenStartPage,padx=10,pady=4,bg ='#ad131a',foreground = '#FFFFFF',activebackground='#ad131a', bd='5', relief='raised')
button5.pack(side = 'bottom', padx = 10)

main.mainloop()   