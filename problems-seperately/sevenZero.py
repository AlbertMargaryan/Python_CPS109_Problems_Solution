def seven_zero(n):
  i = 1
  if n % 2 != 0 and n % 5 != 0:
    while True: 
      d = "7" * i
      if int(d) % n == 0:
        return d
      i += 1
    
  while True:
    j = 0
    while j < i:
      d = "7" * (i - j) + "0" * j
      j+=1
      if int(d) % n == 0:
        return d
    i+=1
