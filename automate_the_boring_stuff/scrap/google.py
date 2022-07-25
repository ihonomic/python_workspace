#! python3
# google.py - Opens several Google search results. - 273page
import requests
import sys
import webbrowser
import bs4

print('Googling...')  # display text while downloading the Google page

# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()

# TODO: Retrieve top search result links.
# TODO: Open a browser tab for each result
webbrowser.open('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
