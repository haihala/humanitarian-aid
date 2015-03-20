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
#root.resizable(0, 0)

# label = Label(root, text="This is a label.")
# text = Text(root)
# button = Button(root, text="This is a button.")

# label.grid()
# text.grid()
# button.grid()

mapFrame = Frame(root, width=650, height=320)
mapFrame.grid(row=1, column=1)

parameterFrame = Frame(root)  # , width=150, height=480)
parameterFrame.grid(row=1, column=2, rowspan=2)
testParameters = Text(parameterFrame)
testParameters.config(height=26, width=20)
testParameters.grid(row=1)
runButton = Button(parameterFrame, text='Run you clever boy.')
runButton.config(bg='red', height=3, font=("Times", 12, "bold"), activebackground='red')
runButton.grid(sticky=N+S+E+W)

infoFrame = Frame(root)  #, width=650, height=160)
infoFrame.grid(row=2, column=1)
testInfo = Text(infoFrame)
testInfo.config(height=10)
testInfo.grid(sticky=W+E+N+S)

os.environ['SDL_WINDOWID'] = str(mapFrame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((650, 320))
screen.fill(pygame.Color(255, 255, 255))
pygame.display.init()
pygame.display.update()

draw()

root.mainloop()

while True:
    pygame.display.update()
