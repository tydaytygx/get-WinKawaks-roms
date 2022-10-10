import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.winkawaks.org/roms/full-rom-list.htm'

r = requests.get(url)
with open('full-rom-list.html', 'w') as file_write:
    file_write.write(r.text)

soup = BeautifulSoup(open("full-rom-list.html"), 'html.parser')
for link in soup.find_all('div', 'rom-system-index-entry-full'):
    print(url + link.next.next.get('href')[:-4] + '-download.htm') # Print the link to verify

    r_download = requests.get(url.split(
        r'/full-rom-list.htm')[0] + '//' + link.next.next.get('href')[:-4] + '-download.htm')
    soup_download = BeautifulSoup(r_download.text, 'html.parser')
    for link_download in soup_download.find_all(target='_blank'): # Get the download link for specific file
        print(link_download.get('href')[2:])
        download_request = requests.get(
                'https://' + link_download.get('href')[2:])
        with open(link_download.string, 'wb') as download_file:
            download_file.write(download_request.content)
        # urllib.request.urlretrieve('https://' + link_download.get('href')[2:], link_download.string) # legacy option
