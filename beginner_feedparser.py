#!/usr/bin/env python2.7
#coding: utf-8

# pip install feedparser

import feedparser

d = feedparser.parse('http://www.reddit.com/r/python/.rss')
#print d['feed']['title']
#print d['feed']['link']
#print d['feed']['subtitle']
#print len(d['entries'])
#print d['entries'][0]['title']
#print d['entries'][0]['link']

#for num,post in enumerate(d.entries):
#    print str(num + 1) + "  " +  post.title + ":" + "\n" + post.link + "\n"

print d.version
print d.headers

