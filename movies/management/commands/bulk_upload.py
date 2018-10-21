# import os
import json
import requests
import getpass

from django.core.management.base import BaseCommand, CommandError

url = 'http://127.0.0.1:8000/api/v1/movies/'
datafile = 'misc/imdb.json'


class Command(BaseCommand):
    help = 'Facilitate bulk upload of resources'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        username = input('Enter Username: ')
        password = getpass.getpass('Password: ')
        with open(datafile) as f: 
            json_data = json.loads(f.read()) 
            for index, each_json in enumerate(json_data, start=1):
                try:
                    requests.post(url, auth=(username, password), data=each_json)
                    if r.status_code == 200:
                        print(index, ']',  each_json['name'])
                except Exception as e:
                    # print(index, ']',  each_json['name'])
                    pass
