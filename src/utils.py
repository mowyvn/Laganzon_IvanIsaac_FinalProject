"""Helper functions for input validation and CLI formatting."""
import os
import platform

yellow = "\033[93m"
green = "\033[92m"
red = "\033[91m"
orange = "\033[38;5;214m"
rst = "\033[0m"

def clear_screen():
    """Clears the terminal screen for Windows, Linux, and macOS."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_valid_energy(prompt, title, artist, genre, mood):
    error_msg = ""
    while True:
        clear_screen()
        titles("ADD SONGS", 1)
        print(f"""Enter song title: {title}
Enter artist name: {artist}
Enter genre: {genre}
Enter mood (e.g., Energetic, Chill, Focused, Happy): {mood}""")
        
        if error_msg:
            print(error_msg)

        user_input = input(prompt).strip()

        if not user_input:
            return None 

        try:
            energy = int(user_input)
            if 1 <= energy <= 10:
                return energy
            error_msg = f"{yellow}Energy level must be between 1 and 10.{rst}"
        except ValueError:
            error_msg = f"{yellow}Invalid number. Please enter an integer.{rst}"

def titles(txt, n):
    """Prints the title at the very top for each option."""
    topt = "‾" * 29 + "\\"
    bott = "_" * 28 + "/"
    sl = int(18 - (len(txt) / 2))
    es = 29 - (sl + len(txt))
    if n == 0:
        print(f"{topt}\n{" " * sl + txt + " " * es + "/"}\n{bott}")
    else:
        print(f"{topt}\n{" " * sl + txt + " " * es + "/"}\n{bott}\nPress Enter[ ↵ ] for back.")

def eb(txt):
    """Waits for any user input before proceeding."""
    input(f"\nPress [ ↵ ] to {txt}.")

