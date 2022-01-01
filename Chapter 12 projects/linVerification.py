
import bs4, requests

url = 'https://tinternet.xyz/'	
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features='html.parser')

counter = 0

for link in soup.select('a[href]'):
	l = link.get('href')
	try:
		requests.get(l).raise_for_status()
	except Exception as exc:
		print('There was a problem at %s ~ %s.' % (l, exc))

	counter += 1


print('All done. We looked at %s links in total.' % str(counter))