import pyautogui
import keyboard
import time

USERNAME = 'Username'

def log_action(action):
    print(f"Performing action: {action}")

def give_item(item):
    log_action(f"give {USERNAME} {item}")
    pyautogui.write(f"give {USERNAME} {item}")
    keyboard.press_and_release("enter")

def open_menu():
    log_action("Opening menu with ` key")
    keyboard.press_and_release('`')

def give_glider():
    open_menu()
    time.sleep(0.01)
    give_item("Glider")
    open_menu()

def give_gun_setup():
    open_menu()
    time.sleep(0.01)
    give_item("Sword")
    time.sleep(0.1)
    give_item("ForcefieldLauncher")
    time.sleep(0.2)
    give_item("Pistol")
    time.sleep(0.2)
    give_item("AK47")
    time.sleep(0.2)
    pyautogui.write("vehicleCollisions off")
    open_menu()

def stop_train():
    open_menu()
    time.sleep(0.01)
    pyautogui.write("trainspeed 0")
    keyboard.press_and_release("enter")
    open_menu()

hotkeys = {
    'g': give_glider,
    'k': give_gun_setup,
    'p': stop_train,
    # TODO:
    # - Sword macro

}

for hotkey, func in hotkeys.items():
    keyboard.add_hotkey(hotkey, func)

# keepalive
while True:
    time.sleep(0.01)