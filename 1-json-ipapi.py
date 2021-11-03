import re
import json
from urllib2 import urlopen
from datetime import date
import time
import sys
import string

today = date.today()

ip_file = open("ip-apis.txt", "r")
isps_file = open("isps.txt", "w")


ips_list = ip_file.readlines()
ip_file.close()

url = "http://ip-api.com/json/"

count = 0
time_counter_start = 0
time_counter_end = 0

isp_dict = {}
isp_dict["Turkcell"] = 0

for ip in ips_list:
    
    #stuff for the 45 request per minute restriction
    if count == 45:
        time_counter_end = time.time()
        time.sleep(61 - time_counter_end + time_counter_start)
        count = 0
        
    if count == 0:
        time_counter_start = time.time()
        
    count = count + 1    

    #creating a new json unit with the wanted fields
    response = urlopen(url + ip)
    data = json.load(response)
    j = {"query" : data["query"], "country" : data["country"], "isp" : data["isp"]}

    #checking if isp is Turkcell's
    if (j["isp"]).encode('utf-8') == "Turkcell Internet" or (j["isp"]).encode('utf-8') == "Tellcom Broadband Network Statement":
        isp_dict["Turkcell"] = isp_dict["Turkcell"] + 1
    else:
        #counting the different isps
        if (j["isp"]).encode('utf-8') not in isp_dict:
            isp_dict[(j["isp"]).encode('utf-8')] = 1
        else:
            isp_dict[(j["isp"]).encode('utf-8')] = isp_dict[(j["isp"]).encode('utf-8')] + 1
        
    
    #writing the collected information into the file "isps.txt"
    isps_file.write(j["query"] + ", " + j["country"] + ", " + j["isp"] + "\n")
    

listoflists = []
for item in isp_dict:
    ll = [item, isp_dict[item]]
    listoflists.append(ll)


chart_file = open("chart_content.js", "a")
chart_file.write( "var var" + str(today).translate(string.maketrans("-","_")) + " = " + format(listoflists) + ";\n" )
chart_file.close()

#------------------------------------------------------------------------
dates = open("dates.js", "a")
dates_string = open("dates_string.js", "a")

dates.write("dates.push( var" + str(today).translate(string.maketrans("-","_")) + ");\n")
dates_string.write("dates_string.push('"+ str(today).translate(string.maketrans("-","_")) + "');\n")

isps_file.close()
