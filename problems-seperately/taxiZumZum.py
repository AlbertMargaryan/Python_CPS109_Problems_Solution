def taxi_zum_zum(moves):
  directions = ["W", "N", "E", "S"]
  currentDirection = "N"
  currentLocaltion = (0, 0)
  
  for move in moves:
    if move == "F":
      x, y = currentLocaltion
      if currentDirection == "N":
        currentLocaltion = (x, y + 1)
      elif currentDirection == "S":
        currentLocaltion = (x, y - 1)
      elif currentDirection == "E":
        currentLocaltion = (x + 1, y)
      elif currentDirection == "W":
        currentLocaltion = (x - 1, y)
    elif move == "L":
      currentDirection = directions[directions.index(currentDirection) - 1]
    elif move == "R":
      currentDirection = directions[directions.index(currentDirection) - 3]
  return currentLocaltion
