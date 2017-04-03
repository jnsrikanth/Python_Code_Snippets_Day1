import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=Coffee+Shops&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")
f = open("CatOut.txt",'w')

#for link in links:
#	print ("<a href='%s'>%s</a>" %(link.get("href"), link.text))

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
        #print (item.contents[0].find_all("a", {"class": "business-name"})[0].text)
        #print (item.contents[1].find_all("p", {"class", "adr"})[0].text)
        f.write((item.contents[0].find_all("a", {"class": "business-name"})[0].text))
        f.write(item.contents[1].find_all("p", {"class", "adr"})[0].text)
        f.write(item.contents[1].find_all("div", {"class", "phones phone primary"})[0].text)

f.close("CatOut.txt")


#f.write(' '.join(('Outputfile', str(var2), ';')))