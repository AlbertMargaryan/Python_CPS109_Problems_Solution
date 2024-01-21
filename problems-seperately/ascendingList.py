
def (list):
  isListAscending = True
  i = 1
  while i < len(list):
    if(list[i] < list[i - 1]):
      isListAscending = False
      break
    i += 1
  return isListAscending
