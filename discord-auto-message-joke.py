import pyautogui
from datetime import datetime
import pytz
import time
import pyjokes

def write_message(datetime, joke):
	pyautogui.write(datetime.strftime("%H:%M:%S")) 
	pyautogui.write(" - ")
	pyautogui.write(joke)
	pyautogui.press('enter')


while True:
	joke = pyjokes.get_joke(language='en', category = 'all') # get a random joke from the pyjokes library

	tz_zurich = pytz.timezone('Europe/Zurich') # set timezone
	datetime_zurich = datetime.now(tz_zurich) # get time
	datetime_zurich.strftime("%H:%M:%S") #format time

	write_message(datetime_zurich, joke) #write the messsage and press enter


	time.sleep(15) # pause (x) amount of seconds until sending the next message

