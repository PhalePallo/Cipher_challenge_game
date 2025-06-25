# Vigenère Cipher Challenge Game

This project is an educational and fun cipher game that challenges users to decrypt messages encrypted using the **Vigenère Cipher**. It is available in two forms:

* CLI-based game (colorful and multiplayer support)
* GUI-based game using **Tkinter** (with themes and interactive interface)

---

## 🧠 Concepts Used

### 1. **Vigenère Cipher**:

* A classical encryption technique using a key to shift letters.
* Built by looping through the key and message.

### 2. **String Manipulation**:

* Conversion between characters and alphabet indexes.
* Handling upper/lowercase and non-alphabet characters.

### 3. **Timers & Multithreading** (CLI):

* Countdown timers with threading for timeout-based input.

### 4. **GUI Programming** with **Tkinter**:

* Interactive widgets (labels, entries, buttons).
* Event-driven logic (on-click callbacks).

### 5. **Dark Mode**:

* Toggle between light and dark UI themes dynamically.

### 6. **High Score Tracking**:

* Saves names and scores to a local file.
* Sorts and displays top scores.

### 7. **Multiplayer Logic** (CLI):

* Turn-based scoring for two players.

---

## 🔍 How the Game Works

### CLI Version

* Randomly generates levels with encrypted messages.
* Prompts user for input with a countdown.
* Score is adjusted for correct, incorrect, and hint usage.
* In multiplayer mode, both players play sequentially.

### GUI Version

* Displays encrypted message on a graphical interface.
* 20-second countdown timer visible.
* Player submits decrypted guess or asks for a hint.
* Scores are updated and stored at the end.
* Theme toggling allows user to switch to dark mode.

---

## 🚀 Features to Add

* 🎮 Level difficulty selection in GUI
* 💾 Save/load progress
* 🌐 Online multiplayer or leaderboard
* 🔒 Custom encryption logic selection (Caesar, ROT13, etc.)
* 📱 Mobile version using Kivy or PyQt
* 🧪 Practice Mode with explanations
* 🎧 Add sound effects on actions

---

## 📦 Installation

```bash
pip install colorama
```

Run CLI:

```bash
python cipher_game.py
```

Run GUI:

```bash
python cipher_gui.py
```

---

## 🧩 Educational Value

This game teaches:

* Cryptography basics
* Python logic and control flow
* GUI design and event handling
* File I/O and data persistence
* Game mechanics and state control
