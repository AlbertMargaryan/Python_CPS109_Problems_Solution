def knight_jump(knight, start, end):
  listKnight = list(knight)
  for i, v in enumerate(start):
    offset = abs(v - end[i])
    if offset in listKnight:
      listKnight.remove(offset)
    else: return False
  return True
