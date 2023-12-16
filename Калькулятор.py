import tkinter as tk

win = tk.Tk()
win.geometry(f"240x220+100+200")
win['bg'] = '#33ffe6'             
win.title("Калькултор")

calc = tk.Entry(win)
calc.grid(row=0,column=0, columnspan=3)

tk.Button(text='1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()
             
