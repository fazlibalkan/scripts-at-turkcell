import re
import json
from urllib2 import urlopen

ip_file = open("ip-apis.txt", "r")
isps_file = open("isps.txt", "w")

ips_list = ip_file.readlines()
ip_file.close()



url = "http://ip-api.com/json/"

for ip in ips_list:
    response = urlopen(url + ip)
    data = json.load(response)
    j = {"query" : data["query"], "country" : data["country"], "isp" : data["isp"]}


    isps_file.write(j["query"] + ", " + j["country"] + ", " + j["isp"] + "\n")
    
    print j["query"] + " | " + j["country"] + " | " + j["isp"]
    
isps_file.close()
