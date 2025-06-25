# cipher_gui.py (GUI version with countdown, high scores)

import tkinter as tk
from tkinter import messagebox
import time
from functools import partial

# --- Cipher Logic ---
def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    key_index = 0

    for char in message:
        if not char.isalpha():
            final += char
        else:
            is_upper = char.isupper()
            char_lower = char.lower()
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.index(char_lower)
            new_index = (index + offset * direction) % len(alphabet)
            new_char = alphabet[new_index]
            final += new_char.upper() if is_upper else new_char
    return final

def encrypt(text, key):
    return vigenere(text, key)

# --- Game Data ---
levels = [
    {"message": "Hello world", "key": "cat"},
    {"message": "Python is fun", "key": "code"},
    {"message": "Security matters", "key": "lock"},
    {"message": "Data is the new oil", "key": "vault"},
    {"message": "Artificial Intelligence", "key": "smart"}
]

score = 0
current_level = 0
timer_seconds = 20
timer_running = False

# --- Score File ---
def save_score(name, score):
    with open("highscores.txt", "a") as f:
        f.write(f"{name},{score}\n")

def show_high_scores():
    try:
        with open("highscores.txt", "r") as f:
            scores = [line.strip().split(",") for line in f]
            scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
            top = "\n".join([f"{i+1}. {name} - {scr}" for i, (name, scr) in enumerate(scores[:5])])
            messagebox.showinfo("High Scores", top)
    except FileNotFoundError:
        messagebox.showinfo("High Scores", "No high scores yet.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Vigenere Cipher Challenge")
root.geometry("500x400")

message_label = tk.Label(root, text="", font=("Courier", 14), wraplength=450)
message_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()

timer_label = tk.Label(root, text="Time left: 20s", font=("Arial", 12))
timer_label.pack()

# Name Input
tk.Label(root, text="Enter your name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack()

# --- Game Functions ---
def load_level():
    global current_level, timer_seconds, timer_running
    if current_level >= len(levels):
        finish_game()
        return

    level = levels[current_level]
    encrypted = encrypt(level["message"], level["key"])
    message_label.config(text=f"Encrypted message: {encrypted}")
    entry.delete(0, tk.END)
    result_label.config(text="")
    timer_seconds = 20
    timer_running = True
    update_timer()

def update_timer():
    global timer_seconds, timer_running
    if timer_seconds > 0 and timer_running:
        timer_label.config(text=f"Time left: {timer_seconds}s")
        timer_seconds -= 1
        root.after(1000, update_timer)
    elif timer_seconds == 0:
        timer_running = False
        result_label.config(text="Time's up!")
        next_level()

def submit_guess():
    global score, current_level, timer_running
    if not timer_running:
        return

    timer_running = False
    user_input = entry.get()
    correct = levels[current_level]["message"]

    if user_input.lower() == correct.lower():
        result_label.config(text="Correct!")
        score += 5
    else:
        result_label.config(text=f"Wrong! Correct: {correct}")
        score -= 1

    score_label.config(text=f"Score: {score}")
    next_level()

def show_hint():
    global score
    key = levels[current_level]["key"]
    result_label.config(text=f"Hint: Key = {key}")
    score -= 2
    score_label.config(text=f"Score: {score}")

def next_level():
    global current_level
    current_level += 1
    root.after(2000, load_level)

def finish_game():
    global score
    name = name_entry.get().strip() or "Anonymous"
    save_score(name, score)
    messagebox.showinfo("Game Over", f"Final Score: {score}")
    show_high_scores()
    root.destroy()

# Buttons
tk.Button(root, text="Submit", command=submit_guess).pack(pady=5)
tk.Button(root, text="Hint (-2 points)", command=show_hint).pack(pady=5)

# --- Start Game ---
load_level()
root.mainloop()
