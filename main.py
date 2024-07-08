import os
import threading
import time
from pathlib import Path

import keyboard
import pyautogui
from dotenv import load_dotenv

env_path = Path('.env')
if env_path.exists():
    load_dotenv()
else:
    print(".env file not found. Please create a .env file with your "
          "ROBLOX_USERNAME.")
    exit(1)

USERNAME = os.getenv("ROBLOX_USERNAME")
if not USERNAME or USERNAME == "YOUR_USERNAME":
    print("Invalid ROBLOX_USERNAME. Please set your username in the "
          ".env file.")
    exit(1)

sword_macro_running = False
sword_macro_thread = None


def read_items_to_give(user):
    items = []
    items_file = Path('items_to_give.txt')
    if items_file.exists():
        with open(items_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    target_user, item = parts
                    target_user = target_user.strip()
                    item = item.strip()
                else:
                    target_user = USERNAME
                    item = parts[0].strip()

                if target_user == user:
                    items.append(item)
    return items


def give_item(item):
    pyautogui.write(f"give {USERNAME} {item}")
    keyboard.press_and_release("enter")


def open_menu():
    keyboard.press_and_release("`")


def give_glider():
    open_menu()
    time.sleep(0.01)
    give_item("Glider")
    open_menu()


def give_gun_setup():
    open_menu()
    time.sleep(0.01)
    items = read_items_to_give(USERNAME)
    for item in items:
        give_item(item)
        time.sleep(0.2)
    pyautogui.write("vehicleCollisions off")
    open_menu()


def stop_train():
    open_menu()
    time.sleep(0.01)
    pyautogui.write("trainspeed 0")
    keyboard.press_and_release("enter")
    open_menu()


def sword_use():
    keyboard.press_and_release("1")
    pyautogui.click()
    time.sleep(0.05)
    keyboard.press_and_release("1")


def sword_macro():
    global sword_macro_running, sword_macro_thread

    def run_macro():
        while sword_macro_running:
            sword_use()
            time.sleep(0.01)

    if sword_macro_running:
        sword_macro_running = False
        sword_macro_thread.join()
        sword_macro_thread = None
    else:
        sword_macro_running = True
        sword_macro_thread = threading.Thread(target=run_macro)
        sword_macro_thread.start()


hotkeys = {
    "F2": give_glider,
    "F5": give_gun_setup,
    "F8": stop_train,
    "F1": sword_macro,
}


def main():
    def hotkey_handler(event):
        if event.name in hotkeys:
            hotkeys[event.name]()

    for hotkey in hotkeys:
        keyboard.hook_key(hotkey, hotkey_handler)

    # Keepalive
    while True:
        time.sleep(0.01)


if __name__ == "__main__":
    main()
