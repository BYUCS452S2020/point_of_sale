import tkinter as tk
from tkinter import messagebox


########### Handlers ############


########## GUI #########
#window
window = tk.Tk()
window.title("point of sale")
#frame to enter upc
text_input_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
text_input_frame.pack()
#frame for button
button_frame = tk.Frame(relief=tk.GROOVE)
button_frame.pack()
#frame to show result
result_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
result_frame.pack()
#frame to show total, reset button
total_frame = tk.Frame(relief=tk.GROOVE, borderwidth=1)
total_frame.pack()



text_input_label = tk.Label(master=text_input_frame, text="input UPC here")
text_input_label.pack(side=tk.LEFT)
text_input_entry = tk.Entry(master=text_input_frame)
text_input_entry.pack(side=tk.RIGHT)

go_button = tk.Button(master=button_frame, text="go")
go_button.pack()

result_label = tk.Label(master=result_frame, text = "Sample product - $26.99")
result_label.pack()

total_cost_label = tk.Label(master=total_frame, text="$74.53")
total_cost_label.pack(side=tk.LEFT)
reset_total_button = tk.Button(master=total_frame, text="reset total")
reset_total_button.pack()

window.mainloop()