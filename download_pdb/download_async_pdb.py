# Author: (c) Sudhanva Naryana

# Import Urllib, Threading, Queue, OS
from urllib.parse import urlparse
import urllib.request
from threading import Thread
import http.client, sys
from queue import Queue
from pathlib import Path
import os

# Check for exisiting file
try:
    os.remove('error.txt')
except OSError:
    pass

# File Handler
url_file = open('url_list.txt')
url_read = url_file.read().replace("'", "")
url_list = url_read.split(",")

# Number of Cuncorrent Processes
concurrent = 500

# Download the files
def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        q.task_done()

# Get status of the file download
def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = http.client.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()

        # PDB Files
        file_name = url.path[10:] + '.pdb'
        request_url = url.scheme + "://" + url.netloc + url.path + '.pdb'
        my_file = Path(file_name)

        if not my_file.is_file():
            # If file exists
            urllib.request.urlretrieve(request_url, file_name)

        return res.status, ourl
    except:
        with open('errors.txt', 'a') as error_file:
            error_file.write(str(ourl) + "\n")
        return "error", ourl

# Print download status
def printStatus(status, url):
    print(status, url)

# Start Queue processing
q = Queue(concurrent * 2)

# Exit on Keyboard Interrupt
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

