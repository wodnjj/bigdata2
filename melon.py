"import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm?dayTime=2022041715'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')
song_list = soup.select('tr[data-song-no]')

for song in song_list:
    rank = song.select_one('.rank').text
    title = song.select_one('.ellipsis.rank01').a.text
    artist = song.select_one('.ellipsis.rank02').a.text
    print(rank, title, artist)