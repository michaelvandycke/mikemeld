import sys
import argparse
import mariadbworker
import requester
import appLogging
import os
import mmap

parser = argparse.ArgumentParser(description='EDL process automation.', usage='%(prog)s [options]')
parser.add_argument('-a','--addurl', help='Add an url, Category name is required', metavar='https://somelist.com/ips.txt -c FEODOTRACKER')
parser.add_argument('-c','--category',help='Category name', metavar='FEODOTRACKER')
parser.add_argument('-r','--run',help='run database automated filling',action='store_true')
parser.add_argument('-t','--testrun',help='DEBUG Purpose',action='store_true')
parser.add_argument('-o','--output',help='Output to file, destination is required', metavar='/var/www/html/')

args = parser.parse_args()

if args.run:
    appLogging.resetLog()
    urlCat = mariadbworker.getAllCat()
    for key in urlCat:
        requester.IpBlockFiller(urlCat[key],key)
    appLogging.logData(4,"Closing")
    sys.exit(0)

if args.addurl:
    if not args.category:
        raise Exception("category name is required")
        appLogging.logData(2,"category name is required for addurl")
        sys.exit(1)
    mariadbworker.insertURL(args.addurl,args.category)
    sys.exit(0)

if args.testrun:
    #if os.path.exists("/var/www"):
    #    print("ok")
    sys.exit(0)

if args.output:
    dic = (mariadbworker.getAllIPCatName()) 
    for ip in dic:
        path = os.path.join(args.output,dic[ip])
        if not os.path.exists(path):
            appLogging.logData(4,"Adding new dir " + path)
            os.mkdir(path)
        with open(args.output+dic[ip]+"/"+dic[ip]+".txt",'a+') as dfile:
            #Enforce content
            if os.path.getsize(args.output+dic[ip]+"/"+dic[ip]+".txt") == 0:
                dfile.writelines(ip+"\n")
            dfile.seek(0)
            if not ip+"\n" in dfile.read():
                dfile.writelines(ip+"\n")
    appLogging.logData(4,"Closing")
    sys.exit(0)
