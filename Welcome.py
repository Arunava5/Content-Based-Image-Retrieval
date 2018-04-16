import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image

labels = []
main = tk.Tk()
main.geometry("1400x900")
main.resizable()

helv36 = font.Font(family='Helvetica', size=12, weight='bold')

main.title("CONTENT BASED IMAGE RETRIEVAL - Final Year Project(U4P04)")
#main.config(bg = '#000000')
main.config(bg = '#ffffff')	
			
path = "nita.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(main, image = img)
panel.pack(side = "top", expand = "no")
panel.image = img

def OpenBrowsePage():
      main.destroy()
      #import BrowseSearchButton
      exec(compile(open("BrowseSearchButton.py").read(), "BrowseSearchButton.py", 'exec'))

           

# TEXT
frame1 = tk.Frame(main)
frame1.pack(pady=10)
frame1.config(bg='#FFFFFF')
label1 = tk.Label(frame1, text = 'National Institute of Technology Agartala',bg='#FFFFFF')
label1.pack(ipadx = 0, ipady = 0, padx = 0, pady = 0)
label1.config(font = ('algerian', 25))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'Jirania, West Tripura',bg='#FFFFFF')
label2.pack(ipadx = 0, ipady = 0, padx = 0, pady = 0)
label2.config(font = ('ariel', 15))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'CBIR System and Classification using Logistic Regression',bg='#FFFFFF')
label2.pack(ipadx = 0, ipady = 10, padx = 0, pady = 0)
label2.config(font = ('ariel', 30))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'Submitted by:',bg='#FFFFFF')
label2.pack(ipadx = 100, ipady = 0, padx = 0, pady = 0)
label2.config(font = ('ariel', 18))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'Arunava Bhattacharjee\nDipanjan Choudhury\nSantanu Das\nManasdeep Deb',bg='#FFFFFF')
label2.pack(ipadx = 100, ipady = 0, padx = 0, pady = 0)
label2.config(font = ('ariel', 14))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'Guided By:',bg='#FFFFFF')
label2.pack(ipadx = 100, ipady = 0, padx = 0, pady = 0)
label2.config(font = ('ariel', 18))

frame2 = tk.Frame(main)
frame2.pack(pady=10)
label2 = tk.Label(frame1, text = 'Mrs. Lalita Kumari\nAssistant Professor, Dept. of Computer Science & Engineering\nNIT Agartala',bg='#FFFFFF')
label2.pack(ipadx = 100, ipady = 0, padx = 0, pady = 0)
label2.config(font = ('ariel', 14))

buttonStart = tk.Button(frame2, text = 'Start',bg ='#18E5EA',activebackground='#18E5EA', font = helv36,padx=30,pady=4, command = OpenBrowsePage)
buttonStart.pack(side = 'left', padx = 10)


			
main.mainloop()