#!/usr/bin/python

"""
Required:
PYTHONPATH="/home/hawkinsw/google-cloud-sdk/lib/"
"""

from __future__ import print_function
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

project_id = "stats-bq"
if __name__=='__main__':
	credentials = GoogleCredentials.get_application_default()
	bigquery_service = build('bigquery', 'v2', credentials=credentials)

	try:
		request = bigquery_service.jobs()
		query = { 'query' : "select count(title) from [publicdata:samples.wikipedia] where title='3M' limit 10" }
		response = request.query(body=query, projectId=project_id).execute()
		for row in response['rows']:	
			print("\t".join(field['v'] for field in row['f']))
	except HttpError as e:
		print("Error: %s", str(e))
