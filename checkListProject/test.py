import tkinter as tk

def on_select(value):
    global selected
    selected = value

    
def submit():
    print("Selected option:" + selected)
    
root = tk.Tk()


options = ["Unset", "1st period", "2nd period", "3rd period", "4th period", "5th period", "6th period", "7th period", "Lunch", "Break"]
dropdown_var = tk.StringVar(value=options[0])

dropdown = tk.OptionMenu(root, dropdown_var, *options, command=on_select)
dropdown.config(font=("Arial", 12))
dropdown.pack()

submit_button = tk.Button(root, text="Submit", command=submit, font=("Arial", 12))
submit_button.pack(pady=10)

root.mainloop()
