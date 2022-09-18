import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# Main root class
class MyUI:
    def __init__(self, parent):
        parent.geometry("310x310")
        parent.title("Sticky Card")
        parent.resizable(False, False)

        # Frame
        frame = ttk.Frame(parent)

        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(2, weight=1)

        # Text
        text = tk.Text(frame, width = 34, height = 15, font = ('Lato'))
        text.grid(row=1,column=0, sticky='w')

        # + (New Card)
        plus = Image.open("plussign.png")

        resized = plus.resize((30,30))

        img = ImageTk.PhotoImage(resized)
        label = ttk.Label(image = img)
        label.image = img

        plus = ttk.Button(frame, text="+", image=label.image, command = self.new_window)
        plus.grid(row=0, column=0, sticky='w')

        # Highlighting
        text.tag_configure("BOLD", font= ('Lato', 14))

        def bold():
            try:
                text.tag_add("BOLD", "sel.first", "sel.last")        
            except tk.TclError:
                pass

        def bld(event):
            try:
                text.tag_add("BOLD", "sel.first", "sel.last")        
            except tk.TclError:
                pass

        def clear():
            text.tag_remove("BOLD", "sel.first", "sel.last")

        def clr(event):
            text.tag_remove("BOLD", "sel.first", "sel.last")

        bold_btn = ttk.Button(frame, text = "Bold", command = bold)
        bold_btn.grid(row=0, column = 0, sticky ='w', padx = 60, ipady = 3)
        text.bind('<Control-b>', bld)
        text.bind('<Alt_L>', clr)

        clear_btn = ttk.Button(frame, text = "Clear", command = clear)
        clear_btn.grid(row=0, column = 0, sticky ='w', padx = 150, ipady = 3)

        # Delete card button
        delete_card = ttk.Button(frame, text="Delete", command = parent.destroy)
        delete_card.grid(row=0, column=0, sticky = 'w', padx = 234, ipady = 6)

        # Frame grid
        frame.grid(row=0,column=0)

    # New window function (+)
    def new_window(self):
        win = Toplevel()
        MyUI(win)


# Running the program
root = Tk()
MyUI(root)
root.mainloop()