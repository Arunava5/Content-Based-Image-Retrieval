from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageTk


root = Tk()






root.title("CONTENT BASED IMAGE RETRIEVAL SYSTEM")

root.geometry("700x700")
root.configure(background='#242424')

w = Label(root, text="CONTENT BASED IMAGE RETRIEVAL", bg="black", fg="white")
w.pack(fill=X,ipadx=50, ipady = 20,pady=50, padx=50)
w.config(font=("Sans Serif", 20))





class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,  text="CHOOSE IMAGE",bg="#545555", fg="#2EFAEB", padx=100,pady=20, command=chooseFile)
                        
                         
    self.button.pack(side=LEFT)





def chooseFile():
      
      ImageFile = fd.askopenfile(parent=root,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
	        
      data=Image.open(ImageFile)
      img=ImageTk.PhotoImage(data)
      Label.config(image=img)
      Label.image=img
      
      ImageFile.close()
	  


class Search:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,  text="SEARCH", bg="#545555", fg="#2EFAEB", padx=100,pady=20, command=chooseFile)
                        
                         
    self.button.pack(side='bottom')


	         
app = App(root)

Label = tkinter.Label(root,image='')


Label.pack()

search = Search(root)




mainloop()