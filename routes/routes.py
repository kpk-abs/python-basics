import csv

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

def readDistanceCSV():
  distances = []
  intColumns = ['Distance']
  with open('Distance.csv', mode='r') as file:
      reader = csv.DictReader(file)
      for distance in reader:
        distance = convertType(intColumns, distance)
        distances.append(distance)
  return distances

def readRoutesCSV():
  routes = []
  arrayColumns = ['Stops']
  with open('Route.csv', mode='r') as file:
      reader = csv.DictReader(file)
      for route in reader:
        route = covertToArray(arrayColumns, route)
        routes.append(route)
  return routes  

def displayDistance(routes, distances):
  routesWithTotalDistance = getComputedDistance(routes, distances)
  print(routesWithTotalDistance)
  
def main():
  distances = readDistanceCSV()
  routes = readRoutesCSV()
  displayDistance(routes, distances)  
  
main()