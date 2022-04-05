import requests
import mariadbworker
import re
import appLogging

def IpBlockFiller(url,category):
    print(url)
    try:
        myRequest = requests.get(url,timeout=5)

        if myRequest.status_code != 200:
            raise Exception("The server is not responding");

        for ipBlock in myRequest.text.splitlines():
            ip = re.findall(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}-{1}(?:[0-9]{1,3}\.){3}[0-9]{1,3}$',ipBlock)
            if ip:
                mariadbworker.insertIPBLOCK(ip[0], category)
                continue
            ip = re.findall(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-2]\d|/3[0-2])?',ipBlock)
            if ip:
                mariadbworker.insertIPBLOCK(ip[0], category)

    except Exception as e:
        appLogging.logData(2,e + " Error with URL: " + url)
