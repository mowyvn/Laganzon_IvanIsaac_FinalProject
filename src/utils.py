"""Helper functions for input validation and CLI formatting."""
import os
import platform

def clear_screen():
    """Clears the terminal screen for Windows, Linux, and macOS."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_valid_energy(prompt):
    """Ensures the user enters a valid integer between 1 and 10."""
    while True:
        try:
            if not (inp := input(prompt)): return
            energy = int(inp)
            if 1 <= energy <= 10:
                return energy
            print("Energy level must be between 1 and 10.")
        except ValueError:
            print("Invalid number. Please enter an integer.")

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

