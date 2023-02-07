import pyautogui as spam
import time
limite_msg = input('Enter numero de msgs: ')
msg = input('coloque a msg: ')

i= 0

time.sleep(0)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press('Enter')
    i+=1