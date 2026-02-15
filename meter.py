# Question: Create a Tkinter VU meter that warns the user when shouting
# Name - ADITYA BHARDWAJ
# Section - D2
# Roll No - 08
# Course – B TECH
# Branch – CSE

import tkinter as tk
import sounddevice as sd
import numpy as np
import math
import time

WIDTH = 400
HEIGHT = 60
MAX_DB = 60
SHOUT_DB = -10
WARNING_COOLDOWN = 2

current_db = -MAX_DB
last_warning_time = 0

root = tk.Tk()
root.title("VU Meter")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack(padx=10, pady=10)

bar = canvas.create_rectangle(0, 0, 0, HEIGHT, fill="lime", width=0)
text = canvas.create_text(
    WIDTH // 2,
    HEIGHT // 2,
    fill="white",
    font=("Consolas", 12, "bold"),
    text="VU: -∞ dB"
)

warning_text = tk.Label(
    root,
    text="",
    fg="red",
    bg="black",
    font=("Consolas", 14, "bold")
)
warning_text.pack(pady=5)

def audio_callback(indata, frames, time_info, status):
    global current_db
    rms = np.sqrt(np.mean(indata ** 2))
    if rms > 0:
        db = 20 * math.log10(rms)
    else:
        db = -MAX_DB
    smoothing = 0.2
    current_db = (1 - smoothing) * current_db + smoothing * max(-MAX_DB, min(0, db))

def update_ui():
    global last_warning_time

    vu_percent = (current_db + MAX_DB) / MAX_DB
    bar_width = int(WIDTH * vu_percent)
    canvas.coords(bar, 0, 0, bar_width, HEIGHT)

    if current_db > SHOUT_DB:
        canvas.itemconfig(bar, fill="red")
        if time.time() - last_warning_time > WARNING_COOLDOWN:
            warning_text.config(text="STOP SHOUTING")
            last_warning_time = time.time()
    elif current_db > -30:
        canvas.itemconfig(bar, fill="yellow")
        warning_text.config(text="")
    else:
        canvas.itemconfig(bar, fill="lime")
        warning_text.config(text="")

    canvas.itemconfig(text, text=f"VU: {int(current_db)} dB")
    root.after(30, update_ui)

stream = sd.InputStream(device=1, channels=1, callback=audio_callback)
stream.start()

update_ui()
root.mainloop()
stream.stop()
