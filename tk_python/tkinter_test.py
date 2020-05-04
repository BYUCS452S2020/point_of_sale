import tkinter as tk
from tkinter import messagebox


value = 1

def handle_do_it():
    global value
    entry_text = entry.get()
    entry.delete(0, tk.END)
    value = value + int(entry_text)
    greeting["text"]= f"{value}"

def handle_close_button():
    window.destroy()

def handle_show_error():
    messagebox.showerror("error title", "error message")

window = tk.Tk()
window.title("point of sale system")

greeting = tk.Label(text=value, width=40)
greeting.pack()

entry=tk.Entry()
#entry.insert(0, value) #uncomment if you want to start with text already in the box
entry.pack()

button = tk.Button(text="add me", command=handle_do_it)
button.pack()

error_button = tk.Button(text="show error", command=handle_show_error)
error_button.pack()

close_button = tk.Button(text="close window", command=handle_close_button)
close_button.pack()

window.mainloop()