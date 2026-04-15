import tkinter as tk
from tkinter import messagebox # <--- NEW IMPORT ADDED HERE
import os
import subprocess
import sys

# --- Base directory ---
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Cross-platform launcher ---
def run_script(relative_path):
    full_path = os.path.join(BASE_DIR, relative_path)
    
    # Normalize path for Windows just to be safe
    full_path = os.path.normpath(full_path)

    # ERROR POPUP 1: File not found
    if not os.path.exists(full_path):
        messagebox.showerror(
            "File Not Found", 
            f"Could not find the script at:\n{full_path}\n\nPlease ensure the 'src' folder is right next to this .exe file!"
        )
        return

    try:
        if sys.platform == "win32":
            # Windows
            subprocess.Popen(
                f'start cmd /k python "{full_path}"',
                shell=True
            )
        elif sys.platform == "darwin":
            # macOS
            script = f'''
            tell application "Terminal"
                activate
                do script "python3 \\"{full_path}\\""
            end tell
            '''
            subprocess.Popen(["osascript", "-e", script])
        else:
            # Linux
            subprocess.Popen(
                ["gnome-terminal", "--", "python3", full_path]
            )

    except Exception as e:
        # ERROR POPUP 2: System execution failed
        messagebox.showerror("Execution Error", f"Failed to launch script:\n{str(e)}")
