from bs4 import BeautifulSoup
from urllib.request import urlopen

def track(link, debug):
	website = "https://www.racenet.com.au"
	website = website + link
	rawSite = urlopen(website)
	rawHTML = rawSite.read()
	soup = BeautifulSoup(rawHTML, "html.parser")

	trackStats = []
	temp = []

	today = soup.find_all('div', attrs={"class":"grid_12 psi"})
	for tag in today:
		linkData = tag.find_all("tr", {"class":"raceDetails"})
		for tag in linkData:
			bold = tag.find_all("span", {"class":"bold"})
			i = 0;
			temp.clear()
			for tag in bold:
				#if debug:
					#print (tag.text)
				temp.append(tag.text)
				i += 1;
			#print(temp);
			'''tempDict = {
				'class' : temp[0],
				'track' : temp[1],
				'time'  : temp[2],
				'other' : temp[3],
				'other2': temp[4],
				'other3': temp[5]
			}'''


			trackStats.append(temp)
	return trackStats;