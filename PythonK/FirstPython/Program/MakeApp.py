import tkinter

MainForm = tkinter.Tk()

def push():
    print('Melon')

#button = tkinter.Button(MainForm, text = 'PUSH').pack(side=tkinter.LEFT)
#button2 = tkinter.Button(MainForm, text = 'PUSH PUSH').pack(side=tkinter.RIGHT)
#button3 = tkinter.Button(MainForm, text = 'BUTTON', width = 20).pack()

button4 = tkinter.Button(MainForm, text = 'Grid1')
button5 = tkinter.Button(MainForm, text = 'Grid2')
button6 = tkinter.Button(MainForm, text = 'Grid3', command=push)

#button4.grid(row = 0, column = 0)
#button5.grid(row = 0, column = 1)
#button6.grid(row = 1, column = 1)

button4.place(x = 0, y = 0)
button5.place(x = 25, y = 25)
button6.place(x = 50, y = 50)

#button.pack()
#button2.pack()
MainForm.mainloop()
