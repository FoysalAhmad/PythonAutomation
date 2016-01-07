#!usr/bin/env
# multithreadedXkcd.py - Downloads XKCD comics using multiple threads

import requests, os,bs4,threading

#os.makedirs('xkcd',exist_ok = True)
try:
	os.makedirs('xkcd')
except OSError:
	if not os.path.isdir('xkcd'):
		raise

def downloadXkcd(startComic,endComic):
	for urlNumber in range(startComic,endComic):
		#downloading the page.
		print('Downloading page http://xkcd.com/%s...'%(urlNumber))
		res = requests.get('http://xkcd.com/%s'%(urlNumber))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)

		comicElem = soup.select('#comic img')

		if comicElem == []:
			print('Could not find comic image.')
		else:
			comicUrl = comicElem[0].get('src')
			#Download the Image
			print('Downloading image %s...',(comicUrl))
			res = requests.get('http:%s'%(comicUrl))
			res.raise_for_status()
			
			#save image to ./xkcd
			imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()



#create and start the thread objects
downloadThreads = []
for i in range(0,1400,100):
	downloadThread = threading.Thread(target=downloadXkcd,args=(i+1,i+99))
	downloadThreads.append(downloadThread)
	downloadThread.start()

#wait for all threads to end
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done.')
