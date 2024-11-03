#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'            # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in x/xkcd
while not url.endswith('#'):
    # Download the page.
    print('Download page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.

    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.
    None
print('Done.')