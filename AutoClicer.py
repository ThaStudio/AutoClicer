import pyautogui as pag
import keyboard
import time
import os

clear = lambda: os.system("cls")
clear()

user_input_timer = float(input("Select Duration (Enter 0 if you do not want duration): ").strip())
print("")

print("Message : Press 'o' open AutoClicer, Press 'i' close AutoClicer.")

while True:
    keyboard.wait("o")
    print("\nMessage : Auto Clicker Open! (Press 'i' close AutoClicer)\n")


    while not keyboard.is_pressed("i"):
        pag.click()
        time.sleep(user_input_timer)

    print("\nMessage : AutoClicer Stoped!\n (Press 'o' open AutoClicer)")
