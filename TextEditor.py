import tkinter as tk
from tkinter import *
from tkinter import ttk



def main():
    
    #Main Window
    window = tk.Tk()
    window.title("Text Editor")
    
    #Scroll Bar
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    
    text_info = Text(window, yscrollcommand=scrollbar.set)
    text_info.pack(fill=BOTH)
    
    scrollbar.config(command=text_info.yview)
    
    
    
    #Opens Window
    window.mainloop()
    
main()