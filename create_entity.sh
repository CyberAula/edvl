curl localhost:1026/v2/entities -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "id": "Room1",
  "type": "Room",
  "temperature": {
    "value": 23,
    "type": "Float"
  },
  "pressure": {
    "value": 720,
    "type": "Integer"
  },
  "temperature_min": {
    "value": 0,
    "type": "Float"
  }
}
EOF

curl http://localhost:1026/v2/entities -s -S -H 'Content-Type: application/json' -d @- <<EOF
{ 
  "id": "ticket",
  "type": "ticket",
  "_id": {
    "type": "String",
    "value": 14
  },
  "mall": {
    "type": "String",
    "value": 1
  },
  "date": {
    "type": "date",
    "value": "01/14/2016"
  },
  "client": {
    "type": "int",
    "value": 77014474650
  },
  "items": {
    "type": "object",
    "value": {}
  }
}
EOF