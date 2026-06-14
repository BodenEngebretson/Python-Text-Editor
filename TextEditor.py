import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename



def init_db():
    
    connection = sqlite3.connect("TextEditorDatabase.db")
    cursor = connection.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT unique NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    connection.commit()
    connection.close()

def auth_user(username_entry, password_entry):
    
    username = username_entry.get().strip()
    password = password_entry.get().strip()


    if not username or not password:
        messagebox.showerror("Error", "All Fields Required!")
        
    connection = sqlite3.connect("TextEditorDatabase.db")
    cursor = connection.cursor()
    
    try:
        
        cursor.execute(
            """INSERT INTO users (username, password) VALUES (?, ?)""",
            (username, password),
        )
        connection.commit()
        messagebox.showinfo("Success", "Account Registered!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"Username '{username}' already exist.")
    finally:
        connection.close()
        
def login_user(username_entry, password_entry):
    
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    connection = sqlite3.connect("TextEditorDatabase.db")
    cursor = connection.cursor()
    
    cursor.execute(
        """ SELECT * FROM users WHERE username = ? and password = ? """,
        (username, password),   
    )
    result = cursor.fetchone()
    connection.close()
    
    if result:
        messagebox.showinfo("Access Granted", f"Welcome Back, {username}!")
    else:
        messagebox.showinfo("Access Denied", "Invalid Username or Password.")



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

def login_window(window):
    login_window = tk.Toplevel(window)
    login_window.title("User Page")
    login_window.geometry("500x500")
    
    #Entries
    # Username Widgets
    tk.Label(login_window, text="Username:", font=("Arial", 10, "bold")).grid(
        row=0, column=0, padx=15, pady=15, sticky="e"
    )
    username_entry = tk.Entry(root, width=25)
    username_entry.grid(row=0, column=1, padx=15, pady=15)
    
    # Password Widgets
    tk.Label(login_window, text="Password:", font=("Arial", 10, "bold")).grid(
        row=0, column=0, padx=15, pady=15, sticky="e"
    )
    password_entry = tk.Entry(root, width=25)
    password_entry.grid(row=0, column=1, padx=15, pady=15)
    


def main():
    
    #Database
    init_db()
    
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
    login = tk.Button(window, text="Login", command= lambda: login_window(window))
    
    
    save.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    login.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    
    
    #Opens Window
    window.mainloop()
    
main()