import requests
import bs4

# r = requests.get('https://google.com')
# ==============
html = open('index.html')
content = html.read()
soup = bs4.BeautifulSoup(content, 'lxml')

heading = soup.select('.heading')
[print(item.getText()) for item in heading]  # get the text
[print(item.get('class')) for item in heading]  # get the classname , 'id'
