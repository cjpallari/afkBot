import pyautogui as pag

import random
import time
import tkinter as tk
from tkinter import messagebox

def on_interrupt():
    messagebox.showinfo("Program Terminated","Program terminated by user")

root = tk.Tk()
root.bind("<Control-c>", lambda event: on_interrupt())



while True:
    x = random.randint(500,700)
    y = random.randint(200,300)

    pag.moveTo(x,y,0.5)
    time.sleep(60)