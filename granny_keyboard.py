#region Imports

import tkinter as tk
import tkinter.font as font
from pynput import keyboard
import random
from pydub import AudioSegment
from pydub.playback import play

#endregion

#region Global variables

# Variable to indicate to open a window
open_window = False

# Variable to indicate to close a window
close_window = False

# Variable to store opened window instances
window_instances = []

#endregion

#region Helper function to convert rgb values to hex, for tkinter background

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

#endregion

#region keypress event handler that runs in a separate thread

def key_press(key):
    if key is not keyboard.Key.backspace:
        # Indicate that we should spawn a window
        global open_window
        open_window = True

        # Play Granny Scream
        sound = AudioSegment.from_wav("./Resources/Granny.wav")
        play(sound)
    else:
        # If the backspace key is pressed, we be kind to the user and remove one granny window
        # Indicate that we should close a window
        global close_window
        close_window = True

#endregion

#region spawn_window() function that controls whether a window is spawned or destroyed, runs on Main thread

def spawn_window():
    global open_window
    global close_window
    global window_instances
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
            x = str(random.randint(100, window.winfo_screenwidth() - 100))
            y = str(random.randint(100, window.winfo_screenheight() - 100))
            window.geometry("300x270+{0}+{1}".format(x, y))

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

            # Add "Granny is watching" label
            lbl = tk.Label(window, text="G̷̛̗͉̬̫̠̰̣͖̫͓̘̥͖̭̖͖̮͙̺̯̣͖͉̦̮̳͇̲͔͊̔̄̀̃̏̔̊́̈́͠r̷̡͎̘͔͇͚̙̙̿̒͌̍̆̈́̌̽́͛͐̓̎̌̇̾̇͒̈́̋̀͛́̈́̓͌͊̑̑͋͒̆̎͒̕͘͜͝͠͝͝a̷̹̻̖̗̩͙̞̣͇̖̹̯̓̔̒͒̈̀͑̃̌̎͑̿͆̌ͅn̶̤̮̟̼̗̫̮̥̱̲̱͕̺̣̩͕̟̯̫̫͍̩͕͗͗̒̃̅͆̑͛̈͘̚n̸̨̨̡̳̖̦̘̝̫̺͇̥͚̝͚͙͖̦̬̜̠̬̟̩̅̈́́͐̊̾̒̅̂̋͌͊̈́̾̍̓̈́̽̊͋̕͝ͅͅy̴̧̛̛̛̼͉̟̰̘̹̖̬̬̦͌͐͊̐̃̀̾̉̈́̒̂̑́̈́̈́͋̀̆́̐̃͑͆̎̎͊̂͊́̽̉̉͂͆͊̉̎̂̾̀͗̚̚͝͝͠ͅ ̴̡͕̼̥̻̩̬̝̺̙̘̬̦̫͍̠̙͙͔̲́̿̈̿͂͆͆̂̂͌̋̓̄͂́̆̀͜͝͠ị̴̢̧̢̢̛̬̩͈̭͖̜̝̳̯̖͎̘͍̙͔̜͕̥̭͖̜͍̩̺̠̭̣͇̭̬͇̫͖̣̖̭͎̳͋͑̽̈́̌͑̃͐̃̈́̚̚͜͜͜͝͠ş̸̧̡̛̪̖̗̍̃́͒̇̉̕͜ͅ ̵͖̙͖̑̏͗̇̔͛̔̚͝w̶̛̖͈͉̟̩̯̖̘͇̭̼̖͈̱̪̌̾̈́̀͋̇̀̈́̔̓͛͊́̅̏̍̍̇̿̄̎͗̈̊̈́͗̀̔̓̿̆̓͂͑̍͘̚̚͘̚a̸̡̡̨̡̛̰͉̭̩̝̬͍͍̮̤̟͚̫͕͈̞̞̿͑̒̀̓́̀̉̔̑̀͗̈́͌̅̀̑͘͘̕̕͠t̷̛̛̛̫̝̳͙̹̓͆̀̈̈́̉̂̽̆̍͊̔̈́̓̿̈́͋̒̆̐̓͑͂͂̓̔́̇͑́̄̉̅̇̚͘͝c̸̨̡̨͇̻̲͎͍͇̲̼̬̫̣̰̻̙͈̯͖͚͇̠̲̤͉̫̣̬̞̑̀̎̇̍͗̂̏̏̎̓̓͋͐̈̊̇̓̅̆͗̈͗̌̏̎̀̿̌̓͘̕͜͜͜͝͝ͅḩ̷͕̙͉̞̞͓̳͖̗͚̞̪͉̮̙̩̯̞̲́̊̈́̏̓͋͆̔́̈̉̐̆͂́̅̀̓̔́͌̀̾͘͘͝͠ͅì̸̢̧̱͈͚̞͔̼̝͓̞̩̫̯̮̮̟̳̮̗̪̳̠̙̜͕̼̂̔̏̅͊̈́̓̎̐̀̉͆̉̀͆̾̓̾͛̎̿̄̊͌́̍̄́͆̄̔̔͊̒̀͛͋̍͒̄͜ň̸̨̨̧̪̫͎̱̟͎̭̦̤͚̬͎̹͖̰͔̲̞̯̯̦͉͓̪̈͑́̎͐͂̈́̈͋̽͊̊̈́̔͋͗̕͘͜͝ͅģ̸͉͈̰̜̰̩̬̰͇̮̟͔̼̦̤̩̌͋̔͐̈́̀̅̄̌̎̌̏̓̊̄̎̌̈̔̍͋̈́͂̿͗͋̉̃́̽͗̊̓̚̚", fg='red', font=("RansomNote", 20), bg=rgbtohex(r=r, g=g, b=b))
            lbl.place(anchor="center", relx=0.5, y=160)

            # Add buttons
            acknowledge_btn = tk.Button(window, text="I acknowledge that Granny is my God", command=window.destroy)
            acknowledge_btn.place(anchor="center", relx=0.5, y=205)
            acknowledge_btn["font"] = font.Font(size=11)

            no_btn = tk.Button(window, text=" No ")
            no_btn.place(anchor="center", relx=0.5, y=245)
            no_btn["state"] = "disabled"
            no_btn["font"] = font.Font(size=11)

            # Add this window to opened window instances array
            window_instances.append(window)

            # Set open_window to false to prevent more windows from opening
            open_window = False

        if close_window == True:
            # Remove the last window
            window_instances[len(window_instances) - 1].destroy()
            window_instances.pop()

            # Set close_window to false
            close_window = False

        # Update root no matter what so stuff doesnt freeze
        root.update()

#endregion

#region Main function

if __name__ == "__main__":
    # Start listening for keypresses
    listener = keyboard.Listener(
        on_press=key_press)
    listener.start()

    # Create a root tk window which is hidden to spawn Granny Windows later
    root = tk.Tk()
    root.withdraw()
    spawn_window()
    root.mainloop()

#endregion