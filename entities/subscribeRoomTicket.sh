curl -v orion:1026/v2/subscriptions -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "description": "A subscription to get RoomTemp for Draco",
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
    	"url": "http://draco:5050/v2/notify"
    },
    "attrs": [
      "pressure",
      "temperature"
    ]
  },
  "expires": "2040-01-01T14:00:00.00Z",
  "throttling": 5
}
EOF