import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_file(window, text_info):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_info.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")
        
def open_file(window, text_info):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if not filepath:
        return
    
    text_info.delete(1.0,tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_info.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def main():
    
    #Main Window
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    
     #Scroll Bar
    scrollbar = Scrollbar(window)
    scrollbar.grid(column=2, sticky="ns")
    
    
    text_info = Text(window, yscrollcommand=scrollbar.set) #This applies it to the root element and sets the y-axis scroll to the scroll bar created earlier
    text_info.grid(row=0, column=1)
    
    scrollbar.config(command=text_info.yview)
    
    #Buttons
    save = tk.Button(window, text="Save", command= lambda: save_file(window, text_info))
    open = tk.Button(window, text="Open", command= lambda: open_file(window, text_info))
    
    save.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    
    #Opens Window
    window.mainloop()
    
main()