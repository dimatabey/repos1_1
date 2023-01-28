from tkinter import*
import math

root= Tk()
root.title="Window"
root.geometry='1500x1500'
canvas=Canvas(root, width = 300, height = 300,bg='white').pack()
oval=canvas.create_oval(15,15,200,200, fill='yellow',activeoutline='black',activewidth=3)

root.mainloop()