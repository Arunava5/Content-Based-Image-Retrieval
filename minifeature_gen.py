import os
import cv2
from img_descriptors import img2modihist
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def gen_dataset(low,high,main):

    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    if os.path.isdir(folder_name):
            messagebox.showinfo( "Error", "Feature vectors for this range exist already!")
            return
    os.mkdir(folder_name)

    file_seghist = open(folder_name+"/seghist.csv","w")

    high += 1
    
    popup = tk.Toplevel()
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    x = (screen_width/2) - 150
    y = (screen_height/2) - 50
    popup.geometry("400x100+%d+%d"%(x,y))
    popup.title("Generating Feature Vectors")	
    tk.Label(popup).grid(row=0,column=0)
    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, length = 400,maximum=high-low)
    progress_bar.grid(row=1, column=0)
    popup.pack_slaves()

    for i in range(low,high):
        filepath = "C:/Users/Arunava/MycvProjects/Corel10k/" + str(i) + ".jpg"

        image = cv2.imread(filepath)
    
        modihist = img2modihist(image)
        modihist = [str(i) for i in modihist]
    
        file_seghist.write("%s,%s\n"%(str(i),",".join(modihist)))     
        popup.update()
        progress += 1
        progress_var.set(progress)
    
    file_seghist.close()
    popup.destroy()
    messagebox.showinfo( "Feature vector Generation", "Feature vectors Generated")