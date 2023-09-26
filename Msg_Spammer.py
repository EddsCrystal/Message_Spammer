import pyautogui
import sys
import time


ms_m = pyautogui.prompt(text='Enter the message', title='Message Spammer', default='')
if ms_m is None:
    pyautogui.alert("Message cannot be null. Program exited")
    sys.exit()


ms_n = pyautogui.prompt(text='Enter no. of messages to send', title='Message Spammer', default='')
if ms_n is None:
    pyautogui.alert("Number of messages cannot be null. Program exited")
    sys.exit()

try:
    ms_n = int(ms_n)
except (ValueError, TypeError):
    pyautogui.alert("Invalid number of messages. Program exited")
    sys.exit()


ms_interval = pyautogui.prompt(text='Enter interval between msgs. (Enter 0 if none)', title='Message Spammer', default='')
if ms_interval is None:
    pyautogui.alert("Interval cannot be null. Program exited")
    sys.exit()

try:
    ms_interval = int(ms_interval)
except (ValueError, TypeError):
    pyautogui.alert("Invalid interval value. Program exited")
    sys.exit()

ms_key = pyautogui.prompt(text='Enter the key which is used to send msgs in all small letters', title='Message Spammer', default='')
if ms_key is None:
    pyautogui.alert("Message key cannot be null. Program exited")
    sys.exit()

ms_con = pyautogui.alert(text='Now select the text box or area where you want to send msgs. Once cursor is set, press OK', title='Message Spammer', button='OK')

if ms_con == "OK":
    for i in range(0, ms_n):
        pyautogui.typewrite(ms_m, interval=ms_interval + 0.01)
        pyautogui.press(ms_key)

time.sleep(1)
pyautogui.alert(text='All messages sent successfully 😄', title='Message Spammer', button='OK')
sys.exit()
