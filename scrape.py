from trackData import track
from getLinks import links
from bs4 import BeautifulSoup
from urllib.request import urlopen

debug = True;

website = "https://www.racenet.com.au/horse-racing-results/"
locData = links(website, False)


raceData = []
for i in len(locData):
	print (track(locData[i]['link'], False))
print (track(locData[0]['link'], False))



#raceData.append(track(locData[0]['link'], debug));
#print (raceData[0])
#print (raceData[-1]

#if debug:
#for i in range (0, len(locData)-1):
#print (track(locData[1]['link'], debug), "\n")
#print (track(locData[1]['link'], debug), "\n")
#print (track(locData[3]['link'], debug))
#	print ("\n")

#final = []
#final.append(track(locData[0]['link'], debug))
#print (final)