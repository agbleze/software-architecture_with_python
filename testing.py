import hashlib
import requests

def get_url_data(url):
    """Return data for a URL"""
    data = requests.get(url).content
    filename = hashlib.md5(url).hexdigest()
    open(filename, "w").write(data)
    return data