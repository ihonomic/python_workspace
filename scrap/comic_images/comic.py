#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ - BEAUTIFUL SOUP DOCUMENTATION

import requests
import bs4
import os

url = 'https://xkcd.com/'
os.makedirs('./scrap/comic_images', exist_ok=True)

while not url.endswith('#'):
    # Download the page
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # URl of the comic
    comicELem = soup.select('#comic img')

    if not comicELem:
        print('No Comic Image found ')
    else:
        imageUrl = comicELem[0].get('src')
        res = requests.get('https:' + imageUrl)
        res.raise_for_status()

        #   save the image
        imageFile = open(os.path.join('./scrap/comic_images',
                                      os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('DONE')

# while not url.endswith('#'):
# # Download the page
# res = requests.get(url)
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'lxml')

# # URl of the comic
# comicELem = soup.select('#comic img')
