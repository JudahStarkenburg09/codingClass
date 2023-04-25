import tkinter as tk

def on_key_press(event):
    global suggest_list, suggest_menu
    current_text = text_widget.get("1.0", "end-1c")
    words = current_text.split()
    last_word = words[-1] if words else ""
    if len(last_word) < 5:
        # Don't suggest until at least 5 letters are typed
        suggest_menu.place_forget()
        return
    matching_items = [item for item in suggest_list if item.startswith(last_word)]
    if matching_items:
        suggest_menu.delete(0, tk.END)
        for item in matching_items:
            suggest_menu.insert(tk.END, item)
        suggest_menu.place(x=text_widget.winfo_x(),
                            y=text_widget.winfo_y() + text_widget.winfo_height())
    else:
        suggest_menu.place_forget()

def on_suggestion_select(event):
    global text_widget, suggest_menu
    selected_text = suggest_menu.get(suggest_menu.curselection())
    text_widget.delete("end-1c linestart", "end")
    text_widget.insert("end-1c", selected_text)
    suggest_menu.place_forget()

root = tk.Tk()
root.geometry('500x500')
suggest_list = ["broken keys", "broken arrow keys", "mouse not working", "bad accessibility settings", "different language", "missing keys", "broken"]

text_widget = tk.Text(root)
text_widget.pack()

suggest_menu = tk.Listbox(root, font=("Arial", 10), width=20, height=4)
suggest_menu.bind("<<ListboxSelect>>", on_suggestion_select)

text_widget.bind("<KeyRelease>", on_key_press)

root.mainloop()
