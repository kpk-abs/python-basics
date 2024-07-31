import csv

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
  
def convertType(intColumns, distance):
  for col in intColumns:
          if col in distance and distance[col]:
            distance[col] = int(distance[col])
  return distance

def readCSV():
  distances = []
  intColumns = ['distance']
  with open('distances.csv', mode='r') as file:
      reader = csv.DictReader(file)
      for distance in reader:
        distance = convertType(intColumns, distance)
        distances.append(distance)
  return distances

def displayDistance(routes, distances):
  routesWithTotalDistance = getComputedDistance(routes, distances)
  print(routesWithTotalDistance)
  
def main():
  distances = readCSV()
  displayDistance(routes, distances)
  
main()