#!   Using multi-threading .
# MultidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading


os.makedirs('./time/xkcd', exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd.
            imageFile = open(os.path.join(
                './time/xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFile.close()


allThreads = []
for i in range(1, 20, 2):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+2))
    # allThreads.append(downloadThread)
    downloadThread.start()
