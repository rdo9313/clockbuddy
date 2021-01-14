from tkinter import *
from logic import Clock

f = open("../../info.txt", "r")
secret1 = f.readline().strip()
secret2 = f.readline().strip()
f.close()

root = Tk()
root.title("Clock Buddy")

def clockIn():
  clock = Clock(secret1, secret2)
  clock.run("ClockIn")

def clockOut():
  clock = Clock(secret1, secret2)
  clock.run("ClockOut")

def checkHistory():
  clock = Clock(secret1, secret2)
  clock.run("hubTime")

enter = Button(root, text="Clock In", bd=5, bg="skyblue", padx=80, pady=80, command=clockIn)
enter.pack(side = LEFT)

leave= Button(root, text="Clock Out", bd=5, bg="red", padx=80, pady=80, command = clockOut)
leave.pack(side = RIGHT)

history= Button(root, text = "History", bd=5, bg="purple", padx=80, pady=80, command =checkHistory)
history.pack(side = BOTTOM)

root.mainloop()