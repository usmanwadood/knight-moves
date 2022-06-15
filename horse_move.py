def GameChallenge(strParam):

  # code goes here
  x = int(strParam[1])
  y = int(strParam[3])
  total = 0

  if x > 8 or y > 8:
    return

  total += lookUp(x, y)
  total +=lookDown(x, y)
  total +=lookLeft(x, y)
  total +=lookRight(x, y)

  return total

# keep this function call here 

def lookUp(x, y):
  
  tot = 0
  up = 0

  if x + 2 > 8:
    return tot
  else:
    up = x + 2

  if y-1 > 0:
    tot += 1
  
  if y+1 <= 8:
    tot += 1

  return tot

def lookDown(x, y):

  tot = 0
  down = 0
  
  if x-2 <= 0:
    return tot
  else:
    down = x - 2

  if y-1 > 0:
    tot += 1
  
  if y+1 <= 8:
    tot += 1

  return tot

def lookLeft(x, y):

  tot = 0
  left = 0

  if y + 2 > 8:
    return tot
  else:
    left = y + 2

  if x-1 > 0:
    tot += 1
  
  if x+1 <= 8:
    tot += 1

  return tot

def lookRight(x, y):

  tot = 0
  right = 0
  
  if y - 2 <= 0:
    return 0
  else:
    right = y - 2

  if x-1 > 0:
    tot += 1
  
  if x+1 <= 8:
    tot += 1

  return tot