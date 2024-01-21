def can_balance(items):
  for i, v in enumerate(items):
    listBefore = (items[:i])[::-1]
    listAfter = items[i+1:]
    
def can_balance(items):
  for i, v in enumerate(items):
    listBefore = items[:i][::-1]
    listAfter = items[i+1:]
    
    beforeSum = sum((j + 1) * a for j, a in enumerate(listBefore))
    afterSum = sum((k + 1) * b for k, b in enumerate(listAfter))

    if beforeSum == afterSum:
      return i
  return -1

    if beforeSum == afterSum:
      return i
  return -1
