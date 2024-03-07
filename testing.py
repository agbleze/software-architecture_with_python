import hashlib
import requests
import os

def get_url_data(url):
    """Return data for a URL"""
    data = requests.get(url).content
    filename = hashlib.md5(url).hexdigest()
    open(filename, "w").write(data)
    return data


def get_url_data_stub(url):
    filename = hashlib.md5(url).hexdigest()
    if os.path.isfile(filename):
        return open(filename).read()
    
## combine both the orginal request and file cache
def get_url_data(url):
    filename = hashlib.md5(url).hexdigest()
    if os.path.isfile(filename):
        return open(filename).read()
    
    data = requests.get(url).content
    open(filename, "w").write(data)
    return data