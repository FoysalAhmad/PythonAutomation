#!usr/env/bin

import requests, bs4

res = requests.get('http://www.livescore.com/')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
#team2 = str(".ply name")
homeTeam = soup.findAll("div", attrs={"class":"ply tright name"})
awayTeam = soup.findAll("div", attrs={"class" : "ply name"})
score = soup.select('.scorelink')
homeTeamNums = len(homeTeam)
#teams = homeTeam + awayTeam
if homeTeamNums != len(awayTeam) or homeTeamNums != len(score):
	pass
favTeam = [u'Barcelona', u'Real Madrid',u'Valencia',u'Atletico Madrid',u'Sevilla',u'Manchester United',
		u'Chelsea',u'Liverpool',u'Arsenal',u'Manchester City',u'Leicester City',u'Tottenham Hotspur',
		u'SSC Napoli',u'Juventus',u'Inter',u'Roma',u'AC Milan',u'Bayern Munich',
		u'Borussia Dortmund',u'Paris Saint Germain']
#minNum = min(len(score),10)
#print(favTeam)
#val  = 'Barcelona' in favTeam
print("\n")
for i in range(len(score)):
	

	hTeam = homeTeam[i].getText(strip = True)
	#print(type(favTeam[6]))
	#print(hTeam)
	#print(type(str(hTeam)))
	#print(type('Foysal'))
	aTeam = awayTeam[i].getText(strip = True)
	#print(type(aTeam))
	#print(aTeam == u'Manchester United')
	#print(str(hTeam) in favTeam)
	#print(str(aTeam) in favTeam)
	#print('Manchester United' in favTeam)
	#val  = aTeam in favTeam
	#print(val)
	#print(str(aTeam) in favTeam)
	#print(type(aTeam.encode('ascii','ignore')))#=='Manchester United')
	if aTeam in favTeam or hTeam in favTeam:
		print(hTeam.ljust(20,' ')+"\t"+score[i].getText()+'\t'+aTeam)
		#print('hi')
#print(awayTeam[1].getText())
print('\n')

