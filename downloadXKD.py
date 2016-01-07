import requests,os,bs4

url = 'http://xkcd.com'
try:
	os.mkdir('xkcd')
except OSError:
	if not os.path.isdir('xkcd'):
		raise

while not url.endswith('#'):
	#Download the page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	# Find the url of the comic image
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image')
	else:
		try:
			comicUrl = 'http:'+comicElem[0].get('src')
			#Download the image
			print ('Downloading image %s...' %(comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			#skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com'+prevLink.get('href')
			continue
			
			# Save the image to ./xkcd.
			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

		# get the prev button's url
		prevLink = soup.select('a[rel = "prev"]')[0]
		url = 'http://xkcd.com'+prevLink.get('href')


print('Done.')