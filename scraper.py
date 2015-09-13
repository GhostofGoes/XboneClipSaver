__author__ = 'Tehlizard'

from lxml import html
import requests
import urllib
import sys
import os
import re
#import bs4

global rem_file

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + rem_file + "...%d%%" % percent)
    sys.stdout.flush()

root_url = 'http://xboxclips.com'
index_url = root_url + '/TehLizard'
download_folder_path = 'C:\\Users\\Tehlizard\\Downloads\\xbone_clips\\'

page = requests.get(index_url)
tree = html.fromstring(page.text)


#soup = bs4.BeautifulSoup(page.text)
#links = [a.attrs.get('href') for a in soup.select('div.video-summary-data a[href^=http]')]

page_urls = tree.xpath('/html/body/div[4]/div/a/@href')
print page_urls


# Main Scraping loop
for video_page_url in page_urls:
    video_page = requests.get(video_page_url)
    video_page_tree = html.fromstring(video_page.text)
    download_url = video_page_tree.xpath('/html/body/div[3]/div[2]/ul/li[6]/a/@href/text()')
    download_url = ''.join(download_url)
    print download_url
    v = video_page_tree.xpath('/html/body/div[3]/div[2]/ul/li[1]//text()')
    v = ''.join(v)
    v = v.replace(":", "")
    video_name = v.replace(' ', '-')
    print video_name
    #file_name = download_folder_path + ''.join(video_name) + '.mp4'
    file_name = os.path.join(download_folder_path, video_name + '.mp4')
    print file_name
    if not os.path.isfile(file_name):
        rem_file = video_name
        urllib.urlretrieve(download_url, file_name) # reporthook=dlProgress
    else:
        print "Error, file \"" + file_name + "\" already exists!"
    #video = requests.get(download_url)
    #with open('C:\\Users\\Tehlizard\\Downloads\\xbone_clips\\' + video_name[10:21] + '.mp4', 'wb') as fd:
    #    fd.write(video.content)