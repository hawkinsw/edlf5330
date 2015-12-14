#!/usr/bin/python

from __future__ import print_function
import pywikibot 
import datetime
import csv

if __name__=='__main__':
	s = datetime.datetime(2015,10,1)
	e = datetime.datetime(2015,11,1)
	count = 0
	with open("500-url-title.csv") as csv_file:
		rdr = csv.reader(csv_file)
		for csv_line in rdr:
			if len(csv_line) == 1 or csv_line[1].replace(" ","") == "":
				continue
			name = csv_line[0]
			url = csv_line[1]
			title = csv_line[2]
			try:
				page = pywikibot.Page(pywikibot.Site(), title)
				revisions = [r for r in page.revisions(reverse=True, starttime=s, endtime=e, changesize=True)]
				revisions_count = len(revisions)
				revisions_size = 0
				revisions_size = sum([int(r['changesize']) for r in revisions])
				revisions_size_magnitude = sum([abs(int(r['changesize'])) for r in revisions])
				if revisions_size != revisions_size_magnitude:
					print("%s: %d vs %d" %(name, revisions_size, revisions_size_magnitude))
					break
				'''			
				for r in revisions:
					print("%s" % str(r))
					print("revisions_count: %d" % revisions_count)
					print("revisions_size: %d" % revisions_size)
				'''
				print("\"%s\",\"%s\",\"%s\",%d,%d" % (name, url, title, revisions_count, revisions_size))
			except UnicodeDecodeError as unicode_e:
				print("%s, -----" % url)
