from tkinter import *

root = Tk()
root.title("Clock Buddy")

def clockIn():
  import clock_in

def clockOut():
  import clock_out


enter = Button(root, text="Clock In", bd=5, bg="skyblue", padx=80, pady=80, command=clockIn)
enter.pack(side = LEFT)

leave= Button(root, text="Clock Out", bd=5, bg="red", padx=80, pady=80, command =clockOut)
leave.pack(side = RIGHT)

root.mainloop()