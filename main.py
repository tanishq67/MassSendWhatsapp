import pywhatkit
import pandas as pd
import time
import pyautogui

def send():
    df = pd.read_csv('contact.csv')

    msg = "The Knowledge Hunt is an initiative of Public Policy and Opinion Cell, IIT Kanpur to engage students at the grass-root level and strengthen the talent pool of our nation in the field of public policy and governance."
    for i in range(0, 4):
        pywhatkit.sendwhatmsg_instantly('+91' + str(df['num'][i]), msg, 5)
        time.sleep(10)
        print("lets print: ")
        pyautogui.moveTo(1870, 1040)
        pyautogui.click()
        print("operation executed -")





if __name__ == '__main__':
    send()
