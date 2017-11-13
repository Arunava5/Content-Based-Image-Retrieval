import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk
import cv2

file = open("ImageNumbers.txt","r")
main = tk.Tk()
main.geometry("900x900")
imgNum = [1,2,3,4,5,6,7,8,9,10]
frame1 = tk.Frame(main)
frame1.pack()
frame2 = tk.Frame(main)
frame2.pack()
frame3 = tk.Frame(main)
frame3.pack()
label = tk.Label(frame1, image = None)
label1 = tk.Label(frame1, text = 'Content Based Image Retrieval')
label1.pack(fill = 'x', ipadx = 30, ipady = 30, padx = 30, pady = 30)
label1.config(fg = 'white', bg = 'black')

class upload:
      def chooseFile():
            ImageFile = fd.askopenfile(parent=main,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
            if ImageFile != None:
                  data = Image.open(ImageFile)
                  img = ImageTk.PhotoImage(data)
                  #canvas = tk.Canvas(width=500,height=400)
                  #canvas.create_image(0,0,image = img)
                  #anvas.image = img
                  #canvas.pack()
                  label.config(image = img, bg = 'cyan')
                  label.image = img
                 
                  ImageFile.close()


      
upload = upload.chooseFile
button = tk.Button(frame1, text = 'Upload image', command = upload)
button.pack()

label.pack(ipadx = 10, ipady = 10, padx = 20, pady = 20)

def search():
      for i in imgNum[:5]:
            #filenum = line
            filename = "Corel10k/"+str(i)+".jpg"
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
      for i in imgNum[6:11]:
            #filenum = line
            filename = "Corel10k/"+str(i)+".jpg"
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


            
button1 = tk.Button(frame2, text = 'Search image', command = search)
button1.pack(padx = 20, pady = 20)
main.mainloop()   