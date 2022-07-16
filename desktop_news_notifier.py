from bs4 import BeautifulSoup
from urllib.request import urlopen
from pyler import notification
import time

url = "address news"

client = urlopen(url)
xml_data = client.read()
client.close()

soup = BeautifulSoup(xml_data, "xml")
news_list = soup.find_all("item")
news_list = news_list[0:5]

for news in news_list:
	notification.notify(title="Daily News", message=news.title.text+"\nPublish On : "+news.pubDate.text, timeout=20)
	time.sleep(1200)