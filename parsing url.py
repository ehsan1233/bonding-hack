import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('https://aachen.firmenkontaktmesse.de/aussteller/')
soup = BeautifulSoup(page)

with open('links.csv','a') as f:
	for link in soup.body.findAll('a', href=True, attrs={'class' : 'w-blog-entry-link'}):
		f.write(link['href'] + "\n")
