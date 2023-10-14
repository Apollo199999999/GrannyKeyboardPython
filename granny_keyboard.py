import tkinter as tk
from pynput import keyboard
import random

window = False

def key_press(key):
    # Indicate to spawn_window() that we should spawn a window
    global window
    window = True

def spawn_window():
    global window
    while True:
        if  window == True:
            # Spawn window on keydown
            window = tk.Toplevel()
            window.title('Granny')
            window.resizable(0, 0)

            # Generate random position
            x = str(random.randint(200, window.winfo_screenwidth() - 200))
            y = str(random.randint(200, window.winfo_screenheight() - 200))
            window.geometry("300x200+{0}+{1}".format(x, y))

            window = False
            
        # Update root no matter what so stuff doesnt freeze up
        root.update()



listener = keyboard.Listener(
    on_press=key_press,)
listener.start()

root = tk.Tk()
root.withdraw()
spawn_window()
root.mainloop()
