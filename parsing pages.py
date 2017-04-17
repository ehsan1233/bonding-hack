import urllib2
from BeautifulSoup import BeautifulSoup

inpPage = open('links.csv','r')
for row in inpPage:
	page = urllib2.urlopen(row)
	soup = BeautifulSoup(page)
	with open('companies_job_pages.csv','a') as links:
		link = soup.body.find('a', href=True, attrs={'rel' : 'nofollow'})
		links.write(link['href'] + '\n')
