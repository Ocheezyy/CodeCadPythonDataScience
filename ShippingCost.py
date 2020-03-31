def grshipcost(weight, premium = 0):
  if premium == 0:
    cost = 20
  else:
    cost = 125
  ppp = 0.0
  if weight <= 2.0:
    return (weight * 1.5) + cost
  elif weight <= 6:
    return (weight * 3.0) + cost
  elif weight <= 10:
    return (weight * 4.0) + cost
  else: 
    return (weight * 4.75) + cost
    
def droneshipcost(weight):
  if weight <= 2.0:
    return (weight * 4.50)
  elif weight <= 6:
    return (weight * 9.0)
  elif weight <= 10:
    return (weight * 12.0)
  else: 
    return (weight * 14.25)
  
def prices(weight):
  print("Ground: " + str(grshipcost(weight)))
  print("Premium ground: " + str(grshipcost(weight, 1)))
  print("Drone: " + str(droneshipcost(weight)))
  
print(prices(41.5))