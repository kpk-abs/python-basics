import csv

distances = [
  {
    "start": 'chennai',
    "end": 'viluppuram',
    "distance": 166,
  },
  {
    "start": 'viluppuram',
    "end": 'trichy',
    "distance": 165,
  },
  {
    "start": 'trichy',
    "end": 'madurai',
    "distance": 138,
  },
  {
    "start": 'madurai',
    "end": 'tirunelveli',
    "distance": 171,
  },
  {
    "start": 'tirunelveli',
    "end": 'kanyakumari',
    "distance": 85,

  },
  {
    "start": 'karur',
    "end": 'trichy',
    "distance": 83,
  },
]

routes = [
  {
    "route": 'chennai-trichy',
    "stops": [
      { "start": 'chennai', "end": 'viluppuram' },
      { "start": 'viluppuram', "end": 'trichy' },
    ],
  },
  {
    "route": 'chennai-karur',
    "stops": [
      { "start": 'chennai', "end": 'viluppuram' },
      { "start": 'viluppuram', "end": 'trichy' },
      { "start": 'trichy', "end": 'karur' },
    ]
  },
  {
    "route": 'trichy-tirunelveli',
    "stops": [
      { "start": 'trichy', "end": 'madurai' },
      { "start": 'madurai', "end": 'tirunelveli' },
    ]
  },
  {
    "route": 'karur-viluppuram',
    "stops": [
      { "start": 'karur', "end": 'trichy' },
      { "start": 'trichy', "end": 'viluppuram' },
    ]
  },
]

def getDistance(stop, distances):
    for distance in distances:
            if(stop["start"] == distance["start"] and stop["end"] == distance["end"]) or (stop["start"] == distance["end"] and stop["end"] == distance["start"]):
                return distance["distance"]
    

def getTotalDistance(route, distances):
    totalDistance = 0
    for stop in route["stops"]:
        totalDistance += getDistance(stop, distances)
    return totalDistance
    
def addTotalDistance(route, distances):
    route["totalDistance"] = getTotalDistance(route,distances)
    return route


def getComputedDistance(routes, distances):
    routesWithDistance = []
    for route in routes:
        routesWithDistance.append(addTotalDistance(route, distances))
    return routesWithDistance

print(getComputedDistance(routes, distances))