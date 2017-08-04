#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" slack_post.py
Single file Slack Post client

"""

import json
import os
import sys

from optparse import OptionParser

try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import urlopen, Request

def main():
    parser = OptionParser()

    parser.add_option("-t", "--text", dest="text", metavar="TEXT")
    parser.add_option("-f", "--file", dest="file", metavar="FILE")
    parser.add_option("-E", "--endpoint", dest="endpoint", metavar="SLACK_ENDPOINT")

    (ops, args) = parser.parse_args()

    text = ops.text
    if (text is None) and (args is not None):
        text = "\n".join(args)

    if ops.file is not None:
        fp = open(ops.file)
        text = fp.read()
        fp.close()

    endpoint = ops.endpoint

    post(text, endpoint)

def post(text, endpoint):
    data = {
        "text": text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    }
    req = Request(endpoint, bytes(json.dumps(data).encode("utf-8")), headers={"Content-type":"application/json"})
    
    urlopen(req)
    
    
if __name__ == "__main__":
    main()
