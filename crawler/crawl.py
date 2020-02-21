#!/usr/bin/env python

'''
Adapted from psuedocode in CLRS chapter 22.2, third edition. This function performs a breadth-first search on the graph. Source for Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
import sys
import requests
import os
import urllib
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin

# needed to access sites. 403 error without user agent
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}


#TODO Take in starting url as argument

#def parseLinks(url, links):
def parseLinks(url):
    try:
        r = requests.get(url, headers=headers)
        page = r.content
        soup = BS(page, 'html.parser')
        #footer = soup.find('ul',{'class':'footer__list row'}).findAll('a')
        links = []
        for link in soup.find('ul',{'class':'footer__list row'}).findAll('a'):
            links.append(urljoin(url, link.get('string')))
            links.append(link.string)
        print (links)
        #print (soup)
    except Exception as e:
        sys.stderr.write("Error: " + str(e))


# Perform BFS on urls until no new urls are found

def bfs(links, start):
    visited = []
    queue = [start]

    while queue:

        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = links[node]

            for neighbor in neighbor:
                queue.append(neighbor)
        return visited

# Publish list to README?

# Future TODO present graphical representation of sites found


start = 'https://northmichigannews.com'

parseLinks(start)
