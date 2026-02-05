from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import os
from pygame import mixer

# Initialize mixer
try:
    mixer.init()
except Exception as e:
    print(f"Warning: Could not initialize mixer: {e}")

root = Tk()
root.geometry("1000x500")
root.title("Dark AI - Intro")

def play_gif():
    """
    Play intro GIF animation
    FIXED: Added error handling for missing GIF file
    """
    gif_file = "zoro.gif"
    
    # Check if GIF file exists
    if not os.path.exists(gif_file):
        print(f"Warning: {gif_file} not found")
        root.destroy()
        return
    
    try:
        root.lift()
        root.attributes("-topmost", True)
        
        global img 
        img = Image.open(gif_file)
        lbl = Label(root)
        lbl.place(x=0, y=0)
        
        # Animate GIF frames
        for frame in ImageSequence.Iterator(img):
            frame = frame.resize((1000, 500))
            frame = ImageTk.PhotoImage(frame)
            lbl.config(image=frame)
            lbl.image = frame  # Keep a reference
            root.update()
            time.sleep(0.05)
        
        root.destroy()
    
    except FileNotFoundError:
        print(f"Error: {gif_file} not found")
        root.destroy()
    except Exception as e:
        print(f"Error playing GIF: {e}")
        root.destroy()

if __name__ == "__main__":
    try:
        play_gif()
        root.mainloop()
    except KeyboardInterrupt:
        print("\nInterrupted")
        root.destroy()
    except Exception as e:
        print(f"Error: {e}")
        if root:
            root.destroy()
