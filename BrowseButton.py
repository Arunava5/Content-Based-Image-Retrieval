import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk

newWindow = tk.Tk()
newWindow.geometry("500x300")

topframe = tk.Frame(newWindow)
topframe.pack()
bottomframe = tk.Frame(newWindow)
bottomframe.pack(side='bottom')
label = tk.Label(topframe, image = None)

def chooseFile():
      ImageFile = fd.askopenfile(parent=newWindow,mode='rb',title='Choose a file', filetypes=[("jpeg files","*.jpg")])
      if ImageFile != None:
         data = Image.open(ImageFile)
         img = ImageTk.PhotoImage(data)
         #canvas = tk.Canvas(width=300,height=300)
         #canvas.create_image(0,0,image = img)
         #canvas.image = img
         #canvas.grid(row=0,column=0)
         label.config(image = img)
         label.image = img
         label.grid(row = 0, column = 1)
         ImageFile.close()

def clear_label():
      label.config(image = '')
      label.image = None
      

button = tk.Button(bottomframe, text = 'Upload image', command = chooseFile)
button.grid(row = 0, column = 0)

button = tk.Button(bottomframe, text = 'Clear image', command = clear_label)
button.grid(row = 0, column = 1)

newWindow.mainloop()   