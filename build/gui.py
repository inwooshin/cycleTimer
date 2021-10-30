from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
import tkinter
import time
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Cycle Timer")
window.overrideredirect(0)

window.geometry("278x291")
window.configure(bg = "#58B5E9")

countSec = 0
countMin = 0
countHour = 0
breakSec = 0
breakMin = 15
toStrTime = '00:10:00'
setUpStart = 0
canvas = 0
count = 0
onMenu = 1

def timeUpCount():
    global countSec, countMin, countHour,toStrTime
    global setUpStart, window, timeText, count, onMenu

    if(onMenu==1):
        #toStrTime = '%02d:%02d:%02d' % (countHour, countMin, countSec)
        if(setUpStart == 1):
            countSec += 1
            if(countSec == 60):
                countSec = 0
                countMin += 1
            if(countMin == 60):
                countMin == 0
                countHour += 1
            timeText.configure(text='%02d:%02d:%02d' % (countHour, countMin, countSec))
            window.after(1000, timeUpCount)
        window.update()
    else :
        menuTitle.configure(text="Study-Time")
        timeText.configure(text='%02d:%02d:%02d' % (countHour, countMin, countSec), font=("맑은 고딕", 47))
        timeText.place(x=20, y=85)
    onMenu = 1


def onClickQuit():
    exit(0)

def onClickUpCount():
    global setUpStart, onMenu

    if(onMenu == 1) :
        setUpStart ^= 1
    else :
        setUpStart = 0
    timeUpCount()

def onClickTakeTime():
    global breakMin
    breakMin -= 1
    timeText.configure(text='%02d:%02d' % (breakMin, breakSec), font=("맑은 고딕", 70 * -1))
    timeText.place(x=50,y=80)
    print('1')

def onClickDownCount():
    global onMenu, onClickTakeTime
    
    if(onMenu == 0):
        timeText.configure(text='%02d:%02d' % (breakMin, breakSec), font=("맑은 고딕", 70 * -1))
    else :
        menuTitle.configure(text="Take a Break")
        timeText.configure(text='%02d:%02d' % (breakMin, breakSec), font=("맑은 고딕", 70 * -1))
        timeText.place(x=50,y=80)
    onMenu = 0


canvas = Canvas(
    window,
    bg = "#58B5E9",
    height = 291,
    width = 278,
    bd = 0,
    highlightthickness = 0,
    relief = "flat"
)

canvas.place(x = 0, y = 0)
countDownImage = PhotoImage(
    file=relative_to_assets("button_1.png"))
countDownButton = Button(
    image=countDownImage,
    borderwidth=0,
    highlightthickness=0,
    command=onClickDownCount,
    relief="flat",
)

countDownButton.place(
    x=51.0,
    y=214.0,
    width=53.0,
    height=45.0
)

countUpImage = PhotoImage(
    file=relative_to_assets("button_4.png"))
countUpButton = Button(
    image=countUpImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=onClickUpCount
)
countUpButton.place(
    x=109.0,
    y=214.0,
    width=53.0,
    height=45.0
)

listImage = PhotoImage(
    file=relative_to_assets("button_3.png"))
listButton = Button(
    image=listImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
listButton.place(
    x=167.0,
    y=214.0,
    width=53.0,
    height=45.0
)

quitImage = PhotoImage(
    file=relative_to_assets("button_2.png"))
quitButton = Button(
    image=quitImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=onClickQuit
)
quitButton.place(
    x=235.0,
    y=10.0,
    width=27.0,
    height=27.0
)

# canvas.create_text(
#     25.0,
#     85.0,
#     anchor="nw",
#     text= toStrTime,
#     fill="#000000",
#     font=("맑은 고딕", 63 * -1)
# )
menuTitle = tkinter.Label(window, text="Up-Counting", font=("맑은 고딕 bold", 16 * -1),
            background='#58B5E9')
menuTitle.place(x=9, y=30)

timeText = tkinter.Label(window, text="00:00:00", font=("맑은 고딕", 47),
            background='#58B5E9')
timeText.place(x=20, y=85)

canvas.create_text(
    12.0,
    16.0,
    anchor="nw",
    text="Timer",
    fill="#000000",
    font=("맑은 고딕", 12 * -1)
)

# canvas.create_text(
#     12.0,
#     33.0,
#     anchor="nw",
#     text="Up-Counting",
#     fill="#000000",
#     font=("맑은 고딕 bold", 16 * -1)
# )


window.resizable(False, False)
window.mainloop()
