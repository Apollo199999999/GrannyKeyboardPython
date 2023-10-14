import tkinter as tk
from pynput import keyboard
import random
from PIL import ImageTk, Image

open_window = False

def key_press(key):
    # Indicate to spawn_window() that we should spawn a window
    global open_window
    open_window = True

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

def spawn_window():
    global open_window
    while True:
        if open_window == True:
            # Spawn window on keydown
            window = tk.Toplevel()
            window.title('Granny')
            window.resizable(0, 0)

            # Set random window background colour
            r = random.randint(0, 255) 
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            window["background"] = rgbtohex(r=r, g=g, b=b)

            # Generate random position
            x = str(random.randint(200, window.winfo_screenwidth() - 200))
            y = str(random.randint(200, window.winfo_screenheight() - 200))
            window.geometry("300x200+{0}+{1}".format(x, y))

            # Draw a stretched Granny face
            # Create a canvas widget
            canvas = tk.Canvas(window, bg=rgbtohex(r=r, g=g, b=b), highlightbackground=rgbtohex(r=r, g=g, b=b), width=260, height=130)
            canvas.place(x=20,y=10)
            background_image = tk.PhotoImage(file="./Resources/Granny.png")
            # This line is necessary as tk.PhotoImage has a bug where it removes the image after, 
            # causing the image to disappear when the window is inactive
            # See https://stackoverflow.com/questions/62910727/displaying-multiple-images-side-by-side-with-tkinter
            canvas.photo = background_image
            canvas.create_image((0,0), anchor="nw", image=background_image)

            open_window = False
            
        # Update root no matter what so stuff doesnt freeze up
        root.update()



listener = keyboard.Listener(
    on_press=key_press,)
listener.start()

root = tk.Tk()
root.withdraw()
spawn_window()
root.mainloop()
