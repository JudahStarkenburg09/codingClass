import tkinter as tk
def timerFunction():
    global timerValue, root

    minutes, seconds = map(int, timerValue.split(":"))

    # Convert minutes and seconds to total seconds
    total_seconds = minutes * 60 + seconds

    # Decrement total seconds
    total_seconds -= 1

    # Calculate new minutes and seconds
    new_minutes = total_seconds // 60
    new_seconds = total_seconds % 60

    # Format the new values
    minutes_str = f"{new_minutes:02d}"
    seconds_str = f"{new_seconds:02d}"

    # Update timerValue
    timerValue = f"{minutes_str}:{seconds_str}"

    print(timerValue)

    if total_seconds > 0:
        # If there are remaining seconds, continue the countdown
        root.after(1000, timerFunction)
    else:
        print("Timer reached 0:00")
        # Perform any actions you want when the timer reaches 0:00

# Example usage
root = tk.Tk()
timerValue = "04:13"  # Initial timer value (5 minutes)
root.after(1000, timerFunction)
root.mainloop()
