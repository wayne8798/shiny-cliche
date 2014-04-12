import Tkinter
from Tkinter import *
import ttk
import tkMessageBox

root  = Tkinter.Tk()
root.geometry("1000x1000")
mainFrame = Frame(root);
def hello():
	tkMessageBox.showinfo("Hello World", "Hello World 2");
	montion_detection.RunCV();


upButton = Button(mainFrame, text = "Up", command=hello, relief = 'flat', background='green')
downButton = Button(mainFrame, text = "Down", command=hello)

ttk.Style().configure("RB.TButton", foreground='red', background='green')
ttk_btn = ttk.Button(mainFrame, text="ttk_Sample", style="RB.TButton")
ttk_btn.pack(side=LEFT)


upButton.pack(side = TOP)
downButton.pack(side = BOTTOM)

mainFrame.pack(fill=BOTH,expand='true')

root.mainloop()