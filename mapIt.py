#! usr/bin/env
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import webbrowser,sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line
	address  = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard
	address = pyperclip.paste()
home = "1775 Milmont Drive Milpitas CA 95035" 
#webbrowser.open('https://www.google.com/maps/place/'+address)
webbrowser.open('https://www.google.com/maps/dir/'+home+'/'+address)

