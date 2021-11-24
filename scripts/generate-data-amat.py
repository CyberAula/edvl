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
        orionEndpoint="orion:1026"
    elif frecuency is None or "":
        frecuency=3
    df = pd.read_csv("/data/original_data_amat_four_checkpoints.csv", sep =",")
    df.head()
    if count==0:
      ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/checkpoint"
      headers = {'Content-Type': 'application/json','charset': 'utf-8'}
      r = requests.get(url = ORION_ENDPOINT)
      if r.status_code!=200 or r.status_code!=201 or r.status_code!=202:
          ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/"
          ngsiEvent={
             'id':'checkpoint',
             'type':'checkpoint',
             '_id':{
                 'type':'string',
                 'value':0
             },
             'area': {
                 'type':'string',
                 'value':0
             },
             'date':{
                 'type':'date',
                 'value':0
             },
             'checkpoint':{
                 'type':'string',
                 'value':0
             },
             'unique_checkpoint':{
                 'type':'string',
                 'value':0
             },
             'geometry':{
                 'type':'object',
                 'value':0
             }
          }
          data = json.dumps(ngsiEvent)
          r = requests.post(url = ORION_ENDPOINT, headers = headers, data = data)

    ORION_ENDPOINT = "http://"+orionEndpoint+"/v2/entities/checkpoint/attrs"
    headers = {'Content-Type': 'application/json','charset': 'utf-8'}
    seed(1)
    # generate some integers
    while (True):
        for _ in range(8736):
            value = randint(0, 8736)
            record=df.iloc[value]
            dateTimeObj=datetime.now()
            ngsiEvent={
               '_id':{
                   'type':'string',
                   'value':record['id']
               },
               'area': {
                   'type':'string',
                   'value':record['area']
               },
               'date':{
                   'type':'date',
                   'value':dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
               },
               'checkpoint':{
                   'type':'string',
                   'value':int(record['checkpoint'])
               },
               'unique_checkpoint':{
                   'type':'string',
                   'value':record['unique_checkpoint']
               },
               'geometry':{
                   'type':'object',
                   'value':record['geometry'].split("(")[1].split(" ")[0]+","+record['geometry'].split(" ")[2].split(")")[0]
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
