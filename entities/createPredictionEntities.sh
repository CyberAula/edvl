curl orion:1026/v2/entities -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "id": "ReqTicketPrediction1",
  "type": "ReqTicketPrediction",
  "predictionId": {
    "value": 0,
    "type": "String"
  },
  "socketId": {
    "value": 0,
    "type": "String"
  },
  "year":{
    "value": 0,
    "type": "Integer"
  },
  "month":{
    "value": 0,
    "type": "Integer"
  },
  "day":{
    "value": 0,
    "type": "Integer"
  },
  "time": {
    "value": 0,
    "type": "Integer"
  },
  "weekDay": {
    "value": 0,
    "type": "Integer"
  }
}
EOF




curl orion:1026/v2/entities -s -S -H 'Content-Type: application/json' -d @- <<EOF
{
  "id": "ResTicketPrediction1",
  "type": "ResTicketPrediction",
  "predictionId": {
    "value": 0,
    "type": "String"
  },
  "socketId": {
    "value": 0,
    "type": "String"
  },
  "predictionValue":{
    "value": 0,
    "type": "Float"
  },
  "year":{
    "value": 0,
    "type": "Integer"
  },
  "month":{
    "value": 0,
    "type": "Integer"
  },
  "day":{
    "value": 0,
    "type": "Integer"
  },
  "time": {
    "value": 0,
    "type": "Integer"
  }
}
EOF


curl orion:1026/v2/entities -s -S -H 'Content-Type: application/json' -d @- <<EOF
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