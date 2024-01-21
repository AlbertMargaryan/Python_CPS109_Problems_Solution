def countDominators(items):
  if items == []:
      return 0
  items.reverse()

  max_i = items[0]
  n = 1
  for x in items:
      if x > max_i:
          max_i = x
          n += 1
  return n
