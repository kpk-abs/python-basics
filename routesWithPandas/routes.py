import pandas as pd

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

def getDistance(stops,ind, distances):
  for distance in distances:
        if(stops[ind] == distance["Start"] and stops[ind+1] == distance["End"]):
                return distance["Distance"]
    

def getTotalDistance(route, distances):
    totalDistance = 0
    stops = route["Stops"]
    for ind in range(len(stops)-1):
      totalDistance += getDistance(stops,ind, distances)
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

def covertToArray(arrayColumns, route):
  for col in arrayColumns:
          if col in route and route[col]:
            route[col] = route[col].split(',')
  return route

def readDistancesCSV():
  distancesAsArray = pd.read_csv('Distance.csv')
  distances = distancesAsArray.to_dict(orient='records')
  return distances

def readRoutesCSV():
  routes = []
  routesAsArray = pd.read_csv('Route.csv')
  modifiedRoutes = routesAsArray.to_dict(orient='records')
  arrayColumns = ['Stops']
  for route in modifiedRoutes:
    route = covertToArray(arrayColumns, route)
    routes.append(route)
  return routes

def displayDistance(routes, distances):
  routesWithTotalDistance = getComputedDistance(routes, distances)
  print(routesWithTotalDistance)
  
def main():
  distances = readDistancesCSV()
  routes = readRoutesCSV()
  displayDistance(routes, distances)
  
main()