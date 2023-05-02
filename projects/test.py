import tkinter as tk
def toggleViewPassword():
    global hidenPassword, checkbutton
    if checkbutton.var.get():
        hidenPassword.config(show = "*")
    else:
        hidenPassword.config(show = "")


root = tk.Tk()
hidenPassword = tk.Entry(root)
hidenPassword.default_show_val = hidenPassword.config(show = "*")
hidenPassword.config(show = "*")
checkbutton = tk.Checkbutton(root, text="Show password", onvalue=False, offvalue=True, command=toggleViewPassword)
checkbutton.var = tk.BooleanVar(value=True)
checkbutton['variable'] = checkbutton.var
hidenPassword.pack()
checkbutton.pack()
tk.mainloop()