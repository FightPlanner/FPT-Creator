import os
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files(startpath):
    with open('tree_structure.fpt', 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write(f"{indent}{os.path.basename(root)}/\n")
            for file in files:
                f.write(f"{indent}    {file}\n")

def select_directory():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        list_files(folder_selected)
        messagebox.showinfo("Information", "FPT file created successfully in the directory of the .py!")

if __name__ == "__main__":
    select_directory()
