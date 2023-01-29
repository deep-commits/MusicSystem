from tkinter import*
root = Tk()
root.geometry("600x800")
f = Frame(root , bg = "Silver" , highlightbackground = "Green", highlightthickness = 5, padx = 200, pady = 50)
f.grid(row = 0, column = 0)

bf = Frame(root, bg = "Wheat", highlightbackground = "Green", highlightthickness = 5, padx = 200, pady = 50)
bf.grid(row = 0, column = 1)

rf = Frame(root, bg = "cyan", highlightbackground = "Green", highlightthickness = 5, padx = 200, pady = 50)
rf.grid(row = 1, column = 0)

lf = Frame(root, bg = "pink", highlightbackground = "Green", highlightthickness = 5, padx = 200, pady = 50)
lf.grid(row = 1, column = 1)

redbutton = Button(f, text = "red", fg = "red")
redbutton.pack(side = LEFT)

bluebutton = Button(bf, text = "blue", fg = "blue")
bluebutton.pack(side = LEFT)

yellowbutton = Button(lf, text = "yellow", fg = "yellow")
yellowbutton.pack(side = LEFT)

orangebutton = Button(rf, text = "orange", fg = "orange")
orangebutton.pack(side = LEFT)

root.mainloop()

