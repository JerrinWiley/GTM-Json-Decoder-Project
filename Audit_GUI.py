import tkinter.filedialog as filedialog
import tkinter as tk
import Auditor
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()

def input():
    input_path = filedialog.askopenfilename(title = "Open GTM Export JSON", initialdir = (os.path.expanduser('~\downloads')), filetypes=[('Json File', '*.json')])
    input_entry.delete(0, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'

def output():
    path = filedialog.askdirectory(title = "Select output folder",initialdir = (os.path.expanduser('~\downloads')))
    output_entry.delete(0, tk.END)  # Remove current text in entry
    output_entry.insert(0, path)  # Insert the 'path'

def begin():
    target_JSON = input_entry.get()
    output_directory = output_entry.get()
    Auditor.audit(target_JSON, output_directory, var1.get())


top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
line = tk.Frame(root, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text='', width=40)
output_entry.insert(0, os.path.expanduser('~\downloads'))
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

begin_button = tk.Button(bottom_frame, text='Begin!', command=lambda:begin())

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)



var1 = tk.IntVar(value=1)
open_output = tk.Checkbutton(bottom_frame, text = 'Automatically open results workbook', variable = var1, onvalue=1, offvalue=0, pady = 5)
open_output.pack()
begin_button.pack(pady=20, fill=tk.X)
root.mainloop()