import tkinter as tk
import os
import subprocess
import sys

# --- Base directory ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --- Cross-platform launcher 
def run_script(relative_path):
    full_path = os.path.join(BASE_DIR, relative_path)

    if not os.path.exists(full_path):
        print(f"ERROR: File not found -> {full_path}")
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
        print("ERROR launching script:", e)


# --- Button actions ---
def salary():
    run_script("src/salary_analysis_zain_alsaleh.py")

def risk():
    run_script("src/risk_analysis_med_ali.py")

def growth():
    run_script("src/growth_analysis_Nadir_Kaci.py")

def skill():
    run_script("src/skill_analysis_Parsa_Siri.py")

def exposure():
    run_script("src/AI_Exposure_index_Hussin_Rashwan.py")

def jobs():
    run_script("src/jobs_by_keyword_Fatah.py")

def summary():
    run_script("src/Data_Summary_Aymen.py")


# --- GUI ---
root = tk.Tk()
root.title("AI Impact on Jobs")
root.geometry("420x520")
root.configure(bg="#1e1e1e")


# --- Title ---
tk.Label(
    root,
    text="AI Impact on Jobs",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
).pack(pady=20)

tk.Label(
    root,
    text="Select a feature",
    font=("Arial", 12),
    fg="lightgray",
    bg="#1e1e1e"
).pack(pady=5)


# --- Button style ---
def make_button(text, command):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 11),
        width=32,
        height=2,
        bg="#2d2d2d",
        fg="white",
        activebackground="#3c3c3c",
        relief="flat"
    )


# --- Buttons ---
make_button("1. Salary Analysis", salary).pack(pady=6)
make_button("2. Automation Risk Analysis", risk).pack(pady=6)
make_button("3. Growth vs Risk Analysis", growth).pack(pady=6)
make_button("4. Search by Skill", skill).pack(pady=6)
make_button("5. AI Exposure Index", exposure).pack(pady=6)
make_button("6. Jobs by Keyword", jobs).pack(pady=6)
make_button("7. Data Summary", summary).pack(pady=6)


# --- Exit ---
tk.Button(
    root,
    text="Exit",
    command=root.quit,
    font=("Arial", 11, "bold"),
    bg="#8b0000",
    fg="white",
    width=32,
    height=2
).pack(pady=20)


# --- Run ---
root.mainloop()
