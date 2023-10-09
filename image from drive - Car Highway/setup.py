import tkinter as tk

def close_window(event):
    if event.keysym == '0':
        root.destroy()

def disable_minimize(event):
    if event.keysym in ('F4', 'm') and (event.state & 0x8):  # Check for Alt key
        return 'break'  # Prevent Alt+F4 and Windows+M

root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.overrideredirect(True)

root.bind('<Key>', close_window)
root.bind('<Key>', disable_minimize)

frame = tk.Frame(root, bg='blue')
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
