__author__ = 'Haihala'
# this is the main file soon to be forgotten until the deadline is far too close.

from Tkinter import *

root = Tk()

root.title("Humanitarian Aid Simulation Model")
root.geometry("800x480")
root.config(bg="grey40")
#root.resizable(0, 0)

# label = Label(root, text="This is a label.")
# text = Text(root)
# button = Button(root, text="This is a button.")

# label.grid()
# text.grid()
# button.grid()

mapFrame = Frame(root)
mapFrame.grid(row=1, column=1)
testMap = Text(mapFrame)
testMap.config(height=20)
testMap.grid()

parameterFrame = Frame(root)
parameterFrame.grid(row=1, column=2, rowspan=2)
testParameters = Text(parameterFrame)
testParameters.config(height=26, width=20)
testParameters.grid(row=1)
runButton = Button(parameterFrame, text='Run you clever boy.')
runButton.config(bg='red', height=3, font=("Times", 12, "bold"), activebackground='red')
runButton.grid(sticky=N+S+E+W)

infoFrame = Frame(root)
infoFrame.grid(row=2, column=1)
testInfo = Text(infoFrame)
testInfo.config(height=10)
testInfo.grid(sticky=W+E+N+S)

root.mainloop()