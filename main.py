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


def read_items_to_give():
    items = {}
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

                if not target_user == "ExampleUser":
                    if target_user in items:
                        items[target_user].append(item)
                    else:
                        items[target_user] = [item]
    return items


def give_item(target_user, item):
    pyautogui.write(f"give {target_user} {item}")
    keyboard.press_and_release("enter")


def open_menu():
    keyboard.press_and_release("`")


def give_glider():
    open_menu()
    time.sleep(0.01)
    give_item(USERNAME, "Glider")
    items_file = Path('glider_extra_users.txt')
    if items_file.exists():
        with open(items_file, 'r') as file:
            for line in file:
                if line != "ExampleUser":
                    time.sleep(0.2)
                    give_item(line, "Glider")
    open_menu()


def give_gun_setup():
    open_menu()
    time.sleep(0.05)
    items = read_items_to_give()
    for user, user_items in items.items():
        for item in user_items:
            give_item(user, item)
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
    for hotkey, func in hotkeys.items():
        keyboard.add_hotkey(hotkey, func)

    # Keepalive
    while True:
        time.sleep(0.01)


if __name__ == "__main__":
    main()
