import csv
import os
from scipy.spatial import distance as dist
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def search(query_features,limit,low,high,main):
    folder_name = "Feature_Vectors(" + str(low) + "-" + str(high) + ")"
    if not os.path.isdir(folder_name):
            messagebox.showinfo( "Search aborted", "Feature vectors for this range don't exist!")
            return []
    results = {}
    featureset_path = folder_name + "/seghist.csv"
    popup = tk.Toplevel()
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x = (screen_width/2) - 150
    y = (screen_height/2) - 50
    popup.geometry("300x100+%d+%d"%(x,y))
    popup.title("Searching.....")	
    tk.Label(popup).grid(row=0,column=0)
    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, length = 300,maximum=high-low)
    progress_bar.grid(row=1, column=0)
    popup.pack_slaves()
        
    with open(featureset_path) as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            count +=1 
            features = [float(x) for x in row[1:]]
            d = dist.euclidean(features,query_features)
            results[row[0]] = d
            popup.update()
            progress += 1
            progress_var.set(progress)
            
    file.close()
    popup.destroy()

    results = sorted([(v,k) for (k,v) in results.items()])
    return [x[1] for x in results[:limit]]        