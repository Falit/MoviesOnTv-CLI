from bs4 import BeautifulSoup as BS
import requests
import traceback


URL="http://tv.burrp.com/search.html?q="
query = raw_input("Enter the movie/actor/actress \n")
url_encoded_query = query.replace(" ","+")

response = requests.get(URL + url_encoded_query)

soup = BS(response.text)
#print soup

results_list = soup.find('table', class_="result")
results = results_list.find_all("tr")
try:
	for result in results:
		time = result.find('td', class_="resultTime")
		date = time.find('span', class_="date")
		frm = time.find('b', class_="from")
		to = time.find('b', class_="to")
		channel = time.find('img')
		title = result.find('td', class_="resultTitle")
		movie = title.find('a', class_="title").strong
		movie_name = movie.contents[0].strip()
		print '\n'.join([movie_name, channel.get('alt'),
						date.contents[0].strip(), frm.contents[0].strip(), 
						to.contents[0].strip()])
		print ''
except:
	pass
	# print traceback.format_exc()
