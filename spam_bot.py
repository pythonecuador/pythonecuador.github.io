# This is a spam bot

import pyautogui,time # This are the two modules needed
# To use pyautogui, if not installed in your pc go to the terminal and type pip install pyautogui

# This is the message which you want to spam
text = "This is a spam BOT!"

# The value 25 is the number of times you want to spam someone

for i in range(25):
    # This 3.5 represents the timegap which u want to send messages.
    time.sleep(3.5)

    pyautogui.typewrite(text)
    pyautogui.press("enter")

# You can change the values accordingly

# If you want to execute it,first run the program and then go to chatbot or anywhere and click your cursor upon it.
# Go destroy your enimies with it!!!🤣🤣🤣🤣
