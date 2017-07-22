import android, os
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

# display
ifs = getIfList()
for i in ifs.keys():
	droid.notify(ifs[i],i)
