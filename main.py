__author__ = 'Haihala'
""" this is the main file soon to be forgotten until the deadline is far too close. """

from Tkinter import *
import pygame
import os


def draw():
    """"This is a function for drawing the map where things move"""
    screen1 = pygame.display.set_mode((100, 100))
    screen1.fill(pygame.Color(255, 0, 255))
    pygame.display.update()

root = Tk()

root.title("Humanitarian Aid Simulation Model")
root.geometry("800x480")
root.config(bg="grey40")
# root.resizable(0, 0)

# label = Label(root, text="This is a label.")
# text = Text(root)
# button = Button(root, text="This is a button.")

# label.grid()
# text.grid()
# button.grid()

mapFrame = Frame(root, width=650, height=320)
mapFrame.grid(row=1, column=1)

parameterFrame = Frame(root)
parameterFrame.grid(row=1, column=2, rowspan=2)
testParameters = Scale(parameterFrame, from_=0, to=200, orient=HORIZONTAL, label="test")
testParameters.grid()
runButton = Button(parameterFrame, text='Run you clever boy.')
runButton.config(bg='red', height=3, font=("Times", 12, "bold"), activebackground='red')
runButton.grid(sticky=N+S+E+W)

infoFrame = Frame(root)
infoFrame.grid(row=2, column=1)
testInfo = Label(infoFrame, text="here is some text that updates based on the slider")
testInfo.grid(sticky=W, row=1, column=1)
data = Label(infoFrame, text=testParameters.get())
data.grid(sticky=W, row=1, column=2)

os.environ['SDL_WINDOWID'] = str(mapFrame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((650, 320))
screen.fill(pygame.Color(255, 255, 255))
pygame.display.init()
pygame.display.update()

draw()


def updateDisplay():
    data.config(text=testParameters.get())
    pygame.display.update()
    root.after(50, updateDisplay)  # reschedule event in 2 seconds

root.after(50, updateDisplay)
root.mainloop()
