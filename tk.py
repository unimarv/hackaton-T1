import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

na_values = [' ']

root = tk.Tk()
root.title("Золотая запись команды PPJC")
root.geometry("600x300")
root.configure(bg='black')
title = tk.Label(root, text="Золотая запись команды PPJC", fg="#00BFFF", bg="black", font=("Arial", 24, "bold"))
title.pack(pady=20)
load_button = tk.Button(root, text="Загрузить", fg="white", bg="#00BFFF", font=("Arial", 16), width=20, height=2)
load_button.pack(pady=50)
root.mainloop()