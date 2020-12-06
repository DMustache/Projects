import sys
import random
from PIL import Image
from PIL import ImageTk
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter import ALL
from tkinter import NW

class Cons:
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27

class Board(Canvas):
    def __init__(self):
        super().__init__(width=Cons.BOARD_WIDTH, \
            height=Cons.BOARD_HEIGHT, bg='blue', highlightthickness=0)
        self.initGame()
        self.pack()
    def initGame(self):
        self.initGame = True
        self.dots = 3
        self.score = 0

        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        self.appleX = 100
        self.appleY = 190

        self.loadImages()

        self.createObjects()
        self.locateApple()
        self.bind_all('<Key>', self.onkeyPressed)
        self.after(Cons.DELAY, self.onTimer)

    def loadImages(self):
        try:
            self.idot = Image.open('dot.png')
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open('head.png')
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open('apple.png')
            self.apple = ImageTk.PhotoImage(self.iapple)

        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self):
        