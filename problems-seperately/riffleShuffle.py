def riffle(list, out = True):
  firstHalf = list[:int(len(list))//2]
  secondHalf = list[int(len(list))//2:]
  riffledList = []
  i = 0
  while i < len(firstHalf):
    if out:
      riffledList.append(firstHalf[i])
      riffledList.append(secondHalf[i])
    else:
      riffledList.append(secondHalf[i])
      riffledList.append(firstHalf[i])
    i+=1  
  return riffledList
