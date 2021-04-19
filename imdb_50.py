from bs4 import BeautifulSoup
import requests


url = 'http://imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_name = []
year = []
rating = []

movie_data = soup.findAll('td', attrs={'class': 'titleColumn'})
movie_data1 = soup.findAll('td', attrs={'class': 'ratingColumn imdbRating'})
movie_data2 = soup.findAll('td', attrs={'class': 'titleColumn'})

for store in movie_data:
    name = store.a.text
    movie_name.append(name)
for store in movie_data1:
    imdb = store.strong.text
    rating.append(imdb)
for store in movie_data2:
    yr = store.span.text
    year.append(yr)


result = [list(zipped) for zipped in zip(movie_name, rating, year)]
str1 = '\n '
final = str1.join([str(elem) for elem in result[:50]])
print(final)

