import time
import threading
from colorama import init, Fore, Style

# Initialize colorama (required for Windows)
init(autoreset=True)

# --- Vigenère Cipher logic ---
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            is_upper = char.isupper()
            char_lower = char.lower()
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.index(char_lower)
            new_index = (index + offset * direction) % len(alphabet)
            new_char = alphabet[new_index]
            final_message += new_char.upper() if is_upper else new_char

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# --- High score saving ---
def save_score(name, score):
    with open("highscores.txt", "a") as file:
        file.write(f"{name},{score}\n")

def show_high_scores():
    try:
        with open("highscores.txt", "r") as file:
            scores = [line.strip().split(",") for line in file]
            scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
            print(Fore.CYAN + "\n🎖 Top Scores:")
            for i, (name, scr) in enumerate(scores[:5]):
                print(Fore.YELLOW + f"{i+1}. {name} - {scr}")
    except FileNotFoundError:
        print(Fore.RED + "No high scores yet.")

# --- Input with timeout using threading ---
def timeout_input(prompt, timeout=20):
    result = [None]

    def get_input():
        result[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print(Fore.RED + "\n⏰ Time's up!")
        return None
    return result[0]

# --- Game Levels (🎮 Added more puzzles) ---
levels = [
    {"message": "Hello world", "key": "cat"},
    {"message": "Python is fun", "key": "code"},
    {"message": "Security matters", "key": "lock"},
    {"message": "Data is the new oil", "key": "vault"},
    {"message": "Artificial Intelligence", "key": "smart"},
    {"message": "Trust no one", "key": "spy"},
    {"message": "Decrypt this fast", "key": "cipher"},
    {"message": "Keep your secrets", "key": "ring"},
    {"message": "Code is poetry", "key": "verse"},
    {"message": "Hack the planet", "key": "matrix"}
]

# --- Game Engine ---
def play_game():
    print(Fore.MAGENTA + "\n🎯 Welcome to the Vigenère Cipher Challenge!")
    print("Decrypt the messages. You have 3 tries and 20 seconds per level.")
    print("Type 'hint' for help (costs 2 points).\n")

    score = 0

    for i, level in enumerate(levels):
        plain = level["message"]
        key = level["key"]
        encrypted = encrypt(plain, key)

        print(Fore.CYAN + f"\n--- Level {i + 1} ---")
        print(Fore.BLUE + f"🔐 Encrypted message: {encrypted}")

        attempts = 3
        while attempts > 0:
            answer = timeout_input(Fore.WHITE + "Your decrypted guess: ", 20)

            if answer is None:
                print(Fore.RED + "❌ Failed due to timeout.")
                break

            if answer.lower() == "hint":
                print(Fore.YELLOW + f"🧩 Hint: The key is '{key}'")
                score -= 2
                continue

            if answer.lower() == plain.lower():
                print(Fore.GREEN + "✅ Correct!")
                score += 5
                break
            else:
                attempts -= 1
                print(Fore.RED + f"❌ Incorrect. Attempts left: {attempts}")

        if attempts == 0:
            print(Fore.LIGHTRED_EX + f"😢 Out of tries! The correct answer was: {plain}")
            score -= 1

        time.sleep(1)

    print(Fore.MAGENTA + "\n🏁 Game Over!")
    print(Fore.GREEN + f"⭐ Final Score: {score} / {len(levels) * 5}")
    name = input(Fore.CYAN + "Enter your name to save your score: ")
    save_score(name, score)
    show_high_scores()

# --- Start Game ---
if __name__ == "__main__":
    play_game()
