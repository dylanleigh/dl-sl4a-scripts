#
# ModeSelect for Android Python
#
# Via a list dialog, quickly toggle bluetooth, silent mode, airport
# mode, screen timeout and so on.
#
# 2011 Dylan Leigh - this code is in the public domain.

import android, sys
droid = android.Android()


def listDialog(title, items):
	'''listdialog - creates a dialog with a list of items, allows user to select one. returns the index selected or None if user pressed back.'''

	droid.dialogCreateAlert(title)
	droid.dialogSetItems(items)
	droid.dialogShow()

	#time.sleep(1) # testing, to view output

	return droid.dialogGetResponse().result['item']


# todo
# wifi, gps toggle
# show if wifi, gps, blue, already on
# one to turn wifi, gps,blue all off

menu = ['Bluetooth toggle', 'Silent toggle', 'Class mode toggle', 'Airport mode toggle', 'Notify stats', 'About']


#                 main starts here

index = listDialog('Mode select', menu)
if (index==None):
	sys.exit()	

# can use return value from dialog to find entry in list, then refer to items by string
result = menu[index]
# alternatively, can use index returned directly for many applications

if (result=='Bluetooth toggle'):
  droid.toggleBluetoothState(None, True)

elif (result=='Silent toggle'):
	droid.toggleRingerSilentMode()

elif (result=='Class mode toggle'):
	if (droid.checkRingerSilentMode()):
		droid.setScreenTimeout(450) 
	else:
		droid.setScreenTimeout(7500)
	droid.toggleRingerSilentMode()

elif (result=='Airport mode toggle'):
   droid.toggleAirplaneMode()

elif (result=='About'):
  droid.notify('modeselect.py', 'by Dylan Leigh 2011 - www.dylanleigh.net')

elif (result=='Notify stats'):
	droid.notify('Battery', str(droid.batteryGetLevel().result))


else:
	droid.makeToast('Not yet implemented')
