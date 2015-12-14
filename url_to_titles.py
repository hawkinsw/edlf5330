#!/usr/bin/python

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2
import csv

def url_to_content(url):
	try:
		data = ""
		#with urllib2.urlopen(url) as opened_url:
		opened_url = urllib2.urlopen(url)
		if opened_url != None:
			for d in opened_url:
				data += d
			return data
		else:
			return None
	except urllib2.URLError as e:
		print("error: %s" % str(e))
		return None

def content_to_title(content):
	if content == None:
		return ""
	soup = BeautifulSoup(content)
	title = soup.find_all(id="firstHeading")
	if len(title) != 1:
		print("Error: Too many titles: %s" ",".join(title));
		return ""
	return title[0].string.encode('utf-8')

if __name__ == '__main__':
	with open("500.csv") as csv_file:
		rdr = csv.reader(csv_file)
		for csv_line in rdr:
			url = csv_line[1]
			name = csv_line[0]
			print("\"%s\",\"%s\",\"%s\"" % (name, url, content_to_title(url_to_content(url))))
