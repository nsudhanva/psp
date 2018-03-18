from urllib.parse import urlparse
import urllib.request
from threading import Thread
import http.client, sys
from queue import Queue
import os

try:
    os.remove('error.txt')
except OSError:
    pass

from pathlib import Path


url_file = open('url_list.txt')
url_read = url_file.read().replace("'", "")
# print(type(url_read))

url_list = url_read.split(",")
# print(type(url_list))
# print(url_list)

concurrent = 500

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        # printStatus(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = http.client.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        # print(url.scheme + "://" + url.netloc + url.path + '.xml')
        file_name = url.path[10:] + '.xml'
        # print(file_name)
        request_url = url.scheme + "://" + url.netloc + url.path + '.xml'
        
        my_file = Path(file_name)
        if not my_file.is_file():
            # file exists
            urllib.request.urlretrieve(request_url, file_name)
            # print(file_name)
        # print(res)
        return res.status, ourl
    except:
        with open('errors.txt', 'a') as error_file:
            error_file.write(str(ourl) + "\n")
        return "error", ourl

def printStatus(status, url):
    print(status, url)

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in url_list:
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)

