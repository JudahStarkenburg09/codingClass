import start
import tkinter as tk
from tkinter import messagebox

def create_window():
    global home_team_dropdown
    window = tk.Tk()
    window.title("Create Graphics")
    window.geometry("400x400")
    window.config(bg='light gray')

    # Checkbox with label and entry box (entry box only enabled if checked): Timer
    timer_var = tk.BooleanVar()
    timer_checkbutton = tk.Checkbutton(window, text="Timer (00:00, minute:second)", variable=timer_var)
    timer_checkbutton.place(x=200, y=20, anchor='center')
    timer_entry = tk.Entry(window, state="disabled")
    timer_entry.config(bg='white', fg='black')
    def toggle_timer_entry():
        if timer_var.get():
            timer_entry.delete(first=0, last=10000)
            timer_entry.config(state="normal")
            timer_entry.config(bg='white', fg='black')
        else:
            timer_entry.delete(first=0, last=10000)
            timer_entry.config(state="disabled")
            timer_entry.config(bg='white', fg='black')
    timer_checkbutton.config(command=toggle_timer_entry)
    timer_checkbutton.config(bg='white', fg='black')
    timer_entry.config(bg='white', fg='black')
    timer_entry.place(x=200, y=50, anchor='center')

    # Checkbox with label: Possession
    possession_var = tk.BooleanVar()
    possession_checkbutton = tk.Checkbutton(window, text="Possession", variable=possession_var)
    possession_checkbutton.config(bg='white', fg='black')
    possession_checkbutton.place(x=200, y=80, anchor='center')

    # Checkbox with label: Switch Sides Possible
    switch_sides_var = tk.BooleanVar()
    switch_sides_checkbutton = tk.Checkbutton(window, text="Switch Sides Possible", variable=switch_sides_var, fg='black', bg='white')
    switch_sides_checkbutton.place(x=200, y=110, anchor='center')

    # Entry box with place holder: Team 1
    team1_entry = tk.Entry(window)
    team1_entry.insert(0, "Home")
    team1_entry.config(bg='white', fg='black')
    team1_entry.place(x=200, y=140, anchor='center')

    # Entry box with place holder: Team 2
    team2_entry = tk.Entry(window)
    team2_entry.insert(0, "Away")
    team2_entry.config(bg='white', fg='black')
    team2_entry.place(x=200, y=160, anchor='center')



    def submit():
        global setText
        print(timer_entry.get())
        all = [timer_var.get(), timer_entry.get(), possession_var.get(), switch_sides_var.get(), team1_entry.get(), team2_entry.get()]
        def finalSubmit():
            root.destroy()
            a = all[0]
            b = all[1]
            c = all[2]
            d = all[3]
            e = all[4]
            f = all[5]
            start.handelGraphics(a, b, c, d, e, f, home_team_var.get())
            
        var1 =  team1_entry.get()
        var2 = team2_entry.get()
        root = tk.Tk()
        root.geometry('200x200')
        root.config(bg='light gray')
        home_team_options = [var1, var2]
        home_team_var = tk.StringVar(value=home_team_options[0])
        home_team_dropdown = tk.OptionMenu(root, home_team_var, *home_team_options)
        home_team_dropdown.config(width=10)
        home_team_dropdown.place(x=100, y=10, anchor='center')
        setText = tk.Label(root, text=f"{home_team_var.get()}")
        setText.place(x=100, y=50, anchor='center')
        def update():
            global setText
            setText.destroy()
            setText = tk.Label(root, text=f"Home Team: {home_team_var.get()}")
            setText.place(x=100, y=50, anchor='center')
            root.after(100, update)
        root.after(10, update)
        submit_button = tk.Button(root, text="Submit", command=finalSubmit, anchor="center")
        submit_button.place(x=100,y=80, anchor='center')
        root.after(100, window.destroy())
        root.mainloop()

    submit_button = tk.Button(window, text="Submit", command=submit, anchor="center")
    submit_button.place(x=200,y=350, anchor='center')

    window.mainloop()

create_window()
