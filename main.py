# Kacper Karabinowski ETI II
# Projekt Zaliczeniowy

import subprocess
import tkinter as tk
from tkinter import font
from tkinter.font import Font
from tkmacosx import Button


def isStart():
    root.destroy()
    subprocess.Popen(['python', 'calculator.py'])


root = tk.Tk()
root.title("Wielki projekt obliczania sieci!")
root.geometry("1200x590")
root.resizable(False, False)

frame = tk.Frame(root, bg="white", width=201, height=198)
frame.grid(row=1, column=4)

custom_font: Font = font.nametofont("TkDefaultFont")
custom_font.configure(size=20)

tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=0, column=0)
(tk.Label(root, text="Aplikacja do obliczania sieci", width=15, height=8, bg="#7B68EE", fg="#fff", wraplength=200,
          font=custom_font)
 .grid(row=0, column=1))
tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=0, column=2)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=0, column=3)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=0, column=4)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=0, column=5)

tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=1, column=0)
(tk.Label(
    root, text="Obliczaj adresy sieci, rozgloszeniowe i adresy hostow",
    width=15, height=8, bg="#7B68EE", fg="#fff", relief="flat", font=custom_font, wraplength=200)
 .grid(row=1, column=1))
tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=1, column=2)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=1, column=3)
# button = Button(
#     frame, text='Zaczynajmy!', bg='#7B68EE',
#     fg='#fff', borderless=1, command=isStart, width=201, height=198,
#     activebackground='#8964D6')
# button.pack()
startButton = tk.Button(root, text='Zaczynajmy!', bg='#7B68EE', fg='#000', command=isStart, width=10, height=5)
startButton.grid(row=1, column=4)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=1, column=5)

tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=2, column=0)
tk.Label(root, width=15, height=8, bg="#7B68EE").grid(row=2, column=1)
(tk.Label(
    root, text="Created by Kacper Karabinowski ETI II rok III semestr",
    width=15, height=8, bg="#7B68EE", fg="#fff", font=custom_font, wraplength=200)
 .grid(row=2, column=2))
tk.Label(root, width=15, height=8, bg="#fff").grid(row=2, column=3)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=2, column=4)
tk.Label(root, width=15, height=8, bg="#fff").grid(row=2, column=5)

root.mainloop()
