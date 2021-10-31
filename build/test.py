import tkinter as tk

def startTimer():
    if(running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()

def stop1(event):
    global running
    running = False
timeText.bind("<Button-1>", stop1)

def start1(event):
    global running
    running = True
timeText.bind("<Button-3>", start1)

startButton = tk.Button(window, text='시작', bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

startButton = tk.Button(window, text='중', bg="yellow", command=stop)
startButton.pack(fill=tk.BOTH)



startTimer()
window.mainloop()