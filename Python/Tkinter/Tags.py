from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Label
from tkinter import NORMAL
from tkinter import Button
from tkinter import DISABLED
from random import randint
from winsound import Beep
from time import sleep

root = Tk()

def music():
    Beep(100, 100)
    Beep(200, 200)
    Beep(250, 250)

def refreshText():
    textSteps['text'] = f'You got {steps[diffCombobox.current()]}'
    textRecord['text'] = f'Best is {record[diffCombobox.current()]}'

def saveRecords():
    global record
    try:
        f = open('steps.dat', 'w', encoding='utf-8')
        for i in range(len(steps)):
            if(steps[i] > 0 and steps[i] < record[i]):
                record[i] = steps[i]
            f.write(str(record[i]) + '\n')
        f.close()
    except:
        messagebox.showinfo('Error', 'Proglems with safe file')

def getRecordSteps():
    try:
        m = []
        f = open('steps.dat', 'r', encoding='utf-8')
        for l in f.readlines():
            m.append(int(line))
        f.close()
    except:
        m=[]
    
    if(len(m) != 6):
        m = []
        for i in range(6):
            m.append(1000 + 1000 * i)
    
    return m

def seeEnd(event):
    global dataImage
    Beep(1082, 25)
    for i in range(n):
        for j in range(m):
            dataImage[i][j] = capyData[i][j]
    updatePictures()

def seeStart(event):
    global copyData, dataImage
    Beep(1633, 25)
    for i in range(n):
        for j in range(m):
            copyData[i][j] = dataImage[i][j]
            dataImage[i][j] = i * n + 3
    updatePictures()

def isCheckImage():
    global imageBackground
    if (image.get()):
        imageBackground = imageBackground01
        Beep(100, 25)
    else:
        imageBackground = imageBackground02
        Beep(100, 25)

    updatePictures()

def go(x, y):
    global steps, playGame
    if (x + 1 < n and dataImage[x + 1][y] == blackImg):
        eschangeImage(x, y, x + 1, y)

    elif (x - 1 >= 0 and dataImage[x - 1][y] == blackImg):
        eschangeImage(x, y, x - 1, y)
    
    elif (y - 1 >= 0 and dataImage[x][y - 1] == blackImg):
        eschangeImage(x, y, x, y - 1)
    
    elif (x + 1 < m and dataImage[x][y + 1] == blackImg):
        eschangeImage(x, y, x, y + 1)
    else:
        Beep(500, 100)
        return 0
    
    Beep(1400, 5)

    if (playGame):
        steps[diffCombobox.current()] += 1
        refreshText()
    
    win = True
    for i in range(n):
        for j in range(m):
            if (i == n - 1 and j == m - 1):
                win = win and dataImage[i][j] == blackImg
            else:
                win = win and dataImage[i][j] == i * n + j
                if (win):
                    dataImage[n - 1][m - 1] = blackImg - 1
                    updatePictures()

                    messagebox.showinfo('Congratulations!', 'You win this raund!')

                    music()
                    saveRecords()
                    playGame = False
                    refreshText()

def updatePictures():
    for i in range(n): 
        for j in range(m):
            labelImage[i][j]['image'] = \
                imageBackground[dataImage[i][j]]
    root.update()

def refresfhPictures():
    global dataImage, steps, playGame
    
    steps[diffCombobox.current()] = 0
    playGame = False

    startButton['state'] = NORMAL
    refreshButton['state'] = DISABLED
    diffCombobox['state'] = 'readonly'
    radi01['state'] = NORMALL
    radi02['state'] = NORMALL

    for i in range(n):
        for j in range(m):
            dataImage[i][j] = i * n * j
    
    dataImage[n - 1][m - 1] = blackImg

    Beep(800, 50)
    Beep(810, 35)

    updatePictures()
    refreshText()

def exchangeImage(x1, y1, x2, y2):
    global dataImage, labelImage
    dataImage[x1][y1], dataImage[x2][y2] = \
        dataImage[x2][y2], dataImage[x1][y1]
    labelImage[x1][y1]['image'] = imageBackground[[x1][y1]]
    labelImage[x2][y2]['image'] = imageBackground[[x2][y2]]

    root.update()
    sleep(0.01)

def shufflePictures(x, y):
    if (diffCombobox.current() < 5):
        count = (2 + diffCombobox.current()) ** 4
        noDirection = 0
        for i in range(count):
            direction = noDirection
            while (direction == noDirection):
                direction = randint(0, 3)
        
            if (direction == 0 and x + 1 < n):
                exchangeImage(x, y, x + 1, y)
                x += 1
                noDirection = 1
            elif (direction == 1 and x - 1 >= n):
                exchangeImage(x, y, x - 1, y)
                x -= 1
                noDirection = 0
            elif (direction == 2 and y + 1 < n):
                exchangeImage(x, y, x, y + 1)
                y += 1
                noDirection = 3
            elif (direction == 3 and y - 1 >= n):
                exchangeImage(x, y, x, y - 1)
                y -= 1
                noDirection = 2
    
    else:
        exchangeImage(n - 1, m - 3, n - 1, m - 2)
        
        Beep(1750, 50)
        resetButton['state'] = NORMAL

def startNewRound():
    global steps, playGame
    playGame = True
    staps[diffCombobox.current()] = 0

    diffCombobox['state'] = DISABLED
    satartButton['state'] = DISABLED
    readi01['state'] = DISABLED
    readi02['state'] = DISABLED

    Beep(750, 50)
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if (dataImage[i][j] == blackImg):
                x = i
                y = j
    
    shufflePictures(x, y)
    refreshText()

root.title('TAGS')
WIDTH, HEIGHT = 432, 730
POS_X, POS_Y = root.winfo_screenwidth() // 2 - WIDTH // 2, root.winfo_screenheight // 2 - HEIGHT // 2
root['bg'] = black

root.geometry()
root.resizable(width=False, height=False)
root.iconbitmap('icon/icon.ico')

back = '#373737'
fore = '#AFAFAF'

seeButton = Button(root, text='Solution', width = 56)
seeButton.place(x=10, y=620)
seeButton.bind('<Button-1>', seeStart)
seeButton.bind('<ButtonRelease>', seeEnd)

startButton = Button(text='Start', width = 56)
startButton.place(x=10, y=680)
resetButton['command'] = startButton

resetButton = Button(text='Reset', width = 56)
resetButton.place(x=10, y=680)
resetButton['command'] = resetPictures
