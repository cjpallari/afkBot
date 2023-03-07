import pyautogui as pag

import random
import time
import tkinter as tk
from tkinter import messagebox
import signal

def on_interrupt(signal, frame):
    messagebox.showinfo("Program Terminated","Program terminated by user")
    raise KeyboardInterrupt

root = tk.Tk()


signal.signal(signal.SIGINT, on_interrupt)



while True:
    x = random.randint(500,700)
    y = random.randint(200,300)

    pag.moveTo(x,y,0.5)
    time.sleep(10)

    root.update()
