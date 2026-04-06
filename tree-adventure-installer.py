import os
import sys
import time
import random
import webbrowser
import ctypes.wintypes
import tkinter as tk

def clear():
    os.system("cls")

def header():
    clear()
    print("="*70)
    print("Treeager's Adventure Installer | heavily edited by Mr. Half-Life")
    print("="*70)
    print()

def terms():
    clear()
    print("TREEAGER'S ADVENTURE TERMS OF CONDITIONS")
    print("-"*60)

    for i in range(50):
        print(f"{i+1}. User accepts pointless rules about trees, squirrels, leaves, and forest data processing.")

    print()
    print("[A] Agree")
    print("[D] Don't Agree")

    choice = input("> ").lower()

    if choice == "d":
        print("fuck you")
        time.sleep(1)
        sys.exit()

    return True


def fake_log():
    logs = [
        "Checking forest assets",
        "Loading bark renderer",
        "Allocating branch physics",
        "Preparing squirrel AI",
        "Compiling leaf shaders",
        "Scanning moss database",
        "Extracting wood textures",
        "Configuring tree collision",
        "Generating forest map",
        "Linking acorn inventory"
    ]
    return random.choice(logs)


def install():
    clear()
    print("Installing Treeager's Adventure\n")

    progress = 0

    while progress < 100:
        progress += random.randint(1,4)
        if progress > 100:
            progress = 100

        bar = "#"*(progress//2)
        print(f"[{bar:<50}] {progress}%  {fake_log()}", end="\r")
        time.sleep(random.uniform(0.05,0.15))

    print()
    time.sleep(1)


def shake_terminal():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))

    x = rect.left
    y = rect.top
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    positions = []

    for _ in range(120):
        positions.append((
            x + random.randint(-300, 300),
            y + random.randint(-200, 200)
        ))

    for px, py in positions:
        ctypes.windll.user32.MoveWindow(hwnd, px, py, width, height, True)
        time.sleep(random.uniform(0.005, 0.03))

    ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)
    
def black_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    root.after(2000, root.destroy)
    root.mainloop()


def bring_terminal_front():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 5)
    ctypes.windll.user32.SetForegroundWindow(hwnd)


def prank_message():
    clear()

    print("\n"*5)
    print("██████  ██████  ███████ ███    ██ ██   ██ ███████ ██████")
    print("██       ██   ██ ██      ████   ██ ██  ██  ██      ██   ██")
    print("██   ███ ██████  █████   ██ ██  ██ █████   █████   ██   ██")
    print("██    ██ ██   ██ ██      ██  ██ ██ ██  ██  ██      ██   ██")
    print(" ██████  ██   ██ ███████ ██   ████ ██   ██ ███████ ██████ ")
    print()
    print("treeager's adventure is not available")
    print("i'm lazy to finish it")
    print()
    print("[F] Fuck Off")
    print("[F] Fuck off")

    input("> ")
    sys.exit()


def main():

    header()

    print("[Y] Install")
    print("[N] Exit")

    choice = input("> ").lower()

    if choice == "n":
        sys.exit()

    if choice == "y":
        terms()
        install()

        shake_terminal()
        black_screen()

        webbrowser.open("https://www.youtube.com/watch?v=xMHJGd3wwZk")
        webbrowser.open("https://www.twitch.tv/a_treeager")

        bring_terminal_front()

        prank_message()


if __name__ == "__main__":
    main()