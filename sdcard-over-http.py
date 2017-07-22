# sdcard-over-http for Android Python

# Quick and dirty script to serve the sdcard over HTTP.
#
#  WARNING:
#  !  Anyone with access to the device                !
#  !  IP can read everything on it, so be careful.    !
#
# Possibly useful for a quick
# backup of a device or other file transfers when you can't use a
# better system.</p>

# 2011 Dylan Leigh - this code is in the Public Domain.

import android, SimpleHTTPServer, os

# this is where files are served from:
docroot = "/sdcard/"

# will use port 8000

droid = android.Android()

def getIfList():
	"""Returns a dict of iface/ip for all up non-loopback interfaces."""
	npipe = os.popen("netcfg")
	ret = {}
	for line in npipe:
		# <ifname> <UP|DOWN> <ip> < netmask>
		# ignore the DOWN ones and loopback
		a = line.split()
		if (a[1] == "UP"):
			if (a[0] != "lo"):
				print line
				ret[a[0]] = a[2]  # ifname = ip
	return ret

# display url(s) to user
ifs = getIfList()
for i in ifs.keys():
  droid.notify("serving sdcard on %s"%(i,), 'http://%s:8000/'%(ifs[i],))

#start server in docroot
os.chdir(docroot)
SimpleHTTPServer.test() 
