from bs4 import BeautifulSoup
from urllib.request import urlopen

website = "https://www.racenet.com.au/horse-racing-results/"
rawSite = urlopen(website);
rawHTML = rawSite.read();
soup = BeautifulSoup(rawHTML, "html.parser")

locData = []


today = soup.find_all('div', attrs={"class":"grid_3 alpha"})
for tag in today:
	linkData = tag.find_all("a", {"class":"link_red"})
	for tag in linkData:
		if debug:
			print ("Location: ", tag.text)
			print ("Link: ", tag["href"], "\n")
		temp = {
			"loc": tag.text,
			"link": tag["href"]
		}
		locData.append(temp);