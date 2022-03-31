from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import webbrowser

# res = requests.get('https://www.edmunds.com/cars-for-sale-by-owner/')
# print(res.raise_for_status)  # Check status response

# Usually we are suppose the access the content with res.text but we need to parse it with bs4
# soup = bs4.BeautifulSoup(res.text, 'lxml')

#
# .getText() - to exclude the tags
# print(text=soup.find_all("h2", {'class': 'header'}))
res = requests.get(
    "https://www.ask.com/web?q=bill%20gate&ad=dirN&qo=homepageSearchBox")
soup = BeautifulSoup(res.text, 'lxml')
result_title = soup.find_all(
    "a", {"class": "PartialSearchResults-item-title-link result-link"})
print(result_title)

#   =======================

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# pprint({
#     "status_code": res.status_code,
#     "type": type(res),
#     "text": res.text[:250]
#     "checkstatusMethod": .raise_for_status()

# })
playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()


#   ========================================

res = requests.get("https://www.google.com/search?q=lionel+messi")
soup = BeautifulSoup(res.text, "lxml")
Elem = soup.select('div a ')
for i in Elem[:6]:
    webbrowser.open(i.get("href"))
