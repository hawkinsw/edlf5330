#!/usr/bin/python

from __future__ import print_function
import Quandl
import csv

class company(object):
	def __init__(self, ticker, url, title, wikipedia_count, wikipedia_volume):
		self.ticker = ticker
		self.url = url
		self.title = title
		self.wikipedia_count = wikipedia_count
		self.wikipedia_volume = wikipedia_volume
		self.stock_volume = None
		self.stock_close = None
	def stripped_ticker(self):
		stripped = self.ticker.replace("NYSE_", "").replace("NASDAQ_", "");
		return stripped
	def __repr__(self):
		return "\"" + self.ticker + "\"," +\
		       "\"" + self.url + "\"," +\
		       "\"" + self.title + "\"," +\
		       "\"" + self.wikipedia_count + "\"," +\
		       "\"" + self.wikipedia_volume + "\"," +\
		       "\"" + str(self.stock_volume) + "\"," +\
		       "\"" + str(self.stock_close) + "\"," +\
		       "\"" + str(abs(float(self.stock_close))) + "\""

def read_sp500():
	sp500 = []	
	with open("500-url-title-wikipedia.csv") as csv_file:
		rdr = csv.reader(csv_file)
		for csv_line in rdr:
			try:
				sp500.append(company(csv_line[0], csv_line[1], csv_line[2], csv_line[3], csv_line[4]))
			except IndexError as ie:
				print("csv_line: %s" % str(csv_line))
				raise ie
			
	return sp500

def main():
	actually_query = True
	query_format = "WIKI/%s"
	sp500 = read_sp500()
	for c in sp500:
		query = query_format % c.stripped_ticker()
		#print("query: %s" % query)
		#continue
		if actually_query:
			'''
			data = Quandl.get(query, collapse='daily', trim_start='2015-10-01', trim_end='2015-10-31', limit=31, authtoken='ZbyrpahXoQapzxxLR8Qe')
			print(data.index)
			sum = 0
			for i,r in data.iterrows():
				print(r['Volume'])
				sum += r['Volume']
			print("sum: %d\n" % sum)
			'''
			try:
				volume_data = Quandl.get(query,
					collapse='daily',
					trim_start='2015-10-01',
					trim_end='2015-10-31',
					row=1,
					limit=1,
					sort_order="desc",
					transformation="cumul",
					authtoken='ZbyrpahXoQapzxxLR8Qe')
				close_data = Quandl.get(query,
					collapse='monthly',
					trim_start='2015-09-01',
					trim_end='2015-10-31',
					row=1,
					limit=1,
					sort_order="desc",
					transformation="rdiff",
					authtoken='ZbyrpahXoQapzxxLR8Qe')
				if 'Volume' in volume_data and len(volume_data['Volume']) > 0:
					c.stock_volume = volume_data['Volume'][0]
				else:	
					c.stock_volume = 'NaN'
				if 'Close' in close_data and len(close_data['Close']) > 0:
					c.stock_close = close_data['Close'][0]
				else:
					c.stock_close = '0.0'
			except Quandl.DatasetNotFound as e:
				c.stock_volume = 'DatasetNotFound'
				c.stock_close = '0.0'
			except Quandl.ErrorDownloading as e:
				c.stock_volume = 'ErrorDownloading'
				c.stock_close = '0.0'
			print("%s" % (c))
		#actually_query = False

main()
