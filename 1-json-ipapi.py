import re
import json
from urllib2 import urlopen

url = "http://ip-api.com/json/24.48.0.1"
response = urlopen(url)
data = json.load(response)

