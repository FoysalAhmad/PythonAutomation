#!usr/bin/env

#lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

#print(' Googling...') 

res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))

res.raise_for_status()

# retrieve top search results links

soup = bs4.BeautifulSoup(res.text)

#open a browser tab for each results

linkElems = soup.select('.r')

numOpen = min(1,len(linkElems))
print(linkElems[0].getText())
#for i in range(numOpen):
	#webbrowser.open('http://google.com'+linkElems[i].get('href'))

