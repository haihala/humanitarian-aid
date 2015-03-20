__author__ = 'Haihala'
# this is the main file soon to be forgotten until the deadline is far too close.

from Tkinter import *

root = Tk()

root.title("Humanitarian Aid Simulation Model")
root.geometry("800x600")
root.config(bg="grey5")

label = Label(root, text="This is a label.")
text = Text(root)
button = Button(root, text="This is a button.")

label.grid()
text.grid()
button.grid()

root.mainloop()