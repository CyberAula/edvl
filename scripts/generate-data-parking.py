#!/usr/bin/python3
import pandas as pd
import os 
import numpy as np
from datetime import datetime
from random import seed
from random import randint
import requests 
import json
import time
import argparse

def generate (frecuency, orionEndpoint):
    count=0
    if orionEndpoint is None:
        orionEndpoint="localhost:1026"
    elif frecuency is None or "":
        frecuency=3
    df = pd.read_csv("./data/datos-parking.csv", sep =",")
    df.head()
    if count==0:
      ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/parking"
      headers = {'Content-Type': 'application/json','charset': 'utf-8'}
      r = requests.get(url = ORION_ENDPOINT)
      if r.status_code!=200 or r.status_code!=201 or r.status_code!=202:
          ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/"
          ngsiEvent={
             'id':'parking',
             'type':'parking',
             'name':{
                 'type':'string',
                 'value':0
             },
             'availableSpotNumber': {
                 'type':'int',
                 'value':0
             },
             'date':{
                 'type':'date',
                 'value':0
             },
             'total': {
                 'type':'int',
                 'value':0
             },
              'available': {
                 'type':'float',
                 'value':0.0
             }
          }
          data = json.dumps(ngsiEvent)
          r = requests.post(url = ORION_ENDPOINT, headers = headers, data = data)

    ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/parking/attrs"
    headers = {'Content-Type': 'application/json','charset': 'utf-8'}
    seed(1)
    # generate some integers 661730
    while (True):
        for _ in range(661730):
            value = randint(0, 661730)
            record=df.iloc[value]
            dateTimeObj=datetime.now()
            ngsiEvent={
               'name':{
                   'type':'string',
                   'value':record['name']
               },
               'availableSpotNumber': {
                   'type':'int',
                   'value':int(record['availableSpotNumber'])
               },
               'date':{
                   'type':'date',
                   'value':dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
               },
               'total':{
                   'type':'int',
                   'value':int(record['total'])
               },
               'available':{
                   'type':'int',
                   'value':int(record['available'])
               }
            }
            print ("Start : %s" % time.ctime())
            time.sleep( frecuency )
            print ("End : %s" % time.ctime())
            data = json.dumps(ngsiEvent)
            print(data)
            r = requests.post(url = ORION_ENDPOINT, headers = headers, data = data) 
        # extracting response text
        #print(r)
            pastebin_url = r.text 
            print("The response is:%s"%pastebin_url)
if __name__== "__main__":
#    parser=argparse.ArgumentParser(
#    description='''Script for collecting tickets from mongoDB ''',
#    epilog="""All's well that ends well.""")
#parser.add_argument('start', type=str, default='2016-01-14', help='Start date for getting tickets!')
#parser.add_argument('end', type=str, default='2016-01-15', help='End date for getting tickets!')
#parser.add_argument('frecuency', type=int, default=5, help='Frecuency for post the tickets to the context broker!')
#parser.add_argument('mongoURI', type=str, default="mongodb://root:example@localhost:27017/", help='mongo uri with format (mongodb://user:password@localhost:27017/) where the dataset is stored!')
#parser.add_argument('orion', type=str, default='localhost:1026', help='host and port of the context broker!')
#args=parser.parse_args()
#os.environ['START_DATE']
    frecuency=os.environ['FRECUENCY'] 
    orion=os.environ['ORION_ENDPOINT'] 
    generate(int(frecuency),orion)
