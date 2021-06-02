curl -v localhost:1026/v2/subscriptions -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "description": "A subscription to get info about Room1",
  "subject": {
   "entities": [
   {
       "id": "Room1",
       "type": "Room"
   }
   ],
   "condition": {
     "attrs": [
     "pressure",
     "temperature"
     ]
 }
},
    "notification": {
    	"http": {
         "url": "http://spark-worker-1:9001"
     },
     "attrs": [
     "temperature",
     "pressure"
     ]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}
EOF

curl -v http://localhost:1026/v2/subscriptions -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "description": "A subscription to get info about the supermarket",
  "subject": {
  "entities": [
    {
      "id": "ticket",
      "type": "ticket"
    }
  ],
  "condition": {
    "attrs": [
      "_id",
      "mall",
      "date",
      "client",
      "items"
    ]
  }
  },
  "notification": {
  "http": {
    "url": "http://spark-worker-1:9001"
  },
  "attrs": [
      "_id",
      "mall",
      "date",
      "client",
      "items"
  ]
  },
  "expires": "2040-01-01T14:00:00.00Z",
  "throttling": 5
}
EOF