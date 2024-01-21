def dominoCycle(list):
  isDomino = True
  for i, v in enumerate(list):
    if i == len(list) - 1:
      if v[1] != list[0][0]:
        isDomino = False
        break
    else:
      if v[1] != list[i + 1][0]:
        isDomino = False
        break
  return isDomino
