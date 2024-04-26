import tkinter as tk
import pygame
from PIL import Image, ImageTk, ImageSequence

def animate_gif(label, idx, frames):
    # Update the label with the next frame
    label.configure(image=frames[idx])
    idx = (idx + 1) % len(frames)
    # Call the function again after a delay
    label.after(100, animate_gif, label, idx, frames)

def play_audio():
    # Load and play the audio file
    pygame.mixer.music.load("rickroll.mp3")
    pygame.mixer.music.play()

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file and play it
pygame.mixer.music.load("rickroll.mp3")
pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Rickroll")

# Load the GIF frames
gif_path = "rickroll.gif"
gif = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

# Create a label to display the animated GIF
gif_label = tk.Label(root)
gif_label.pack(pady=10)

# Start the animation
animate_gif(gif_label, 0, frames)

# Run the main event loop
root.mainloop()
