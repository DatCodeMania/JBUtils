import pyautogui
import keyboard
import time

USERNAME = 'Your Name'


def give_item(item):
    pyautogui.write(f"give {USERNAME} {item}")


def give_glider():
    pyautogui.press("`")
    time.sleep(0.1)
    give_item("Glider")
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.press("`")


def give_gun_setup():
    pyautogui.press("`")
    time.sleep(0.1)
    give_item("Sword")
    time.sleep(0.1)
    give_item("Forcefield_launcher")
    time.sleep(0.1)
    give_item("Pistol")
    time.sleep(0.1)
    give_item("AK47")
    pyautogui.press("`")


hotkeys = {
    'g': give_glider,
    'k': give_gun_setup,
    # TODO:
    # - Sword macro
    # - Movement of invite
    # - Trainstop
}

for hotkey, func in hotkeys.items():
    keyboard.add_hotkey(hotkey, func)


# keepalive
while True:
    time.sleep(1)
