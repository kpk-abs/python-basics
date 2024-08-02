import pandas as pd

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

def covertToArray(arrayColumns, route):
  for col in arrayColumns:
          if col in route and route[col]:
            route[col] = route[col].split(',')
  return route

def readCSV(fileName):
  dataAsArray = pd.read_csv(fileName)
  data = dataAsArray.to_dict(orient='records')
  return data

def processRoutes(routesFromCSV):
  routes = []
  arrayColumns = ['Stops']
  for route in routesFromCSV:
    route = covertToArray(arrayColumns, route)
    routes.append(route)
  return routes

def readDistancesCSV():
  return readCSV('Distance.csv')

def readRoutesCSV():
  routesFromCSV = readCSV('Route.csv')
  return processRoutes(routesFromCSV)

def displayDistance(routes, distances):
  routesWithTotalDistance = getComputedDistance(routes, distances)
  print(routesWithTotalDistance)
  
def main():
  distances = readDistancesCSV()
  routes = readRoutesCSV()
  displayDistance(routes, distances)
  
main()