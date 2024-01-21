def colourTrio(color):
  colorList = list(color)
  newColorList = []
  if len(colorList) == 1:
    return colorList[0]
  for i, v in enumerate(colorList):
    if i + 1 != len(colorList):
      v2 = colorList[i + 1]
      if v == v2:
        newColorList.append(v)
      elif (v == "r" or v2 == "r") and (v == "b" or v2 == "b"):
        newColorList.append("y")
      elif (v == "y" or v2 == "y") and (v == "b" or v2 == "b"):
        newColorList.append("r")
      elif (v == "r" or v2 == "r") and (v == "y" or v2 == "y"):
        newColorList.append("b")
  return colourTrio("".join(newColorList))
