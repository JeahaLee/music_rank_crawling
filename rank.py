from bs4 import BeautifulSoup
import requests

url ="https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01"
resource = requests.get(url)

soup = BeautifulSoup(resource.text,"html.parser")
infos = soup.select("table.list.trackList.byChart p.title")
titles=list()
for i in infos:
    title =i.text.rstrip().lstrip()
    titles.append(title)

artists = list()
infos = soup.select("table.list.trackList.byChart p.artist")
for i in infos:
    artist = i.text.rstrip().lstrip()
    #데이터 처리... \r 같은 거
    flag = artist.find(chr(10))
    if flag !=-1:
        artist = artist[0:flag]
    artists.append(artist)

for i in range(100):
    print((i+1),"위 : ",titles[i] ,", ",artists[i])