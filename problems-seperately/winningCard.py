def winning_card(trick, trump = None):
  if trump is None:
    return winning_card(trick, trick[0][1])
  else:
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
  
    trumpCards = []
    for x,y in trick:
      if trump in y:
        trumpCards.append((x,y))
    if trumpCards != []:
      maxCardNum = 0
      maxCard = ""
      for card in trumpCards:
        if int(vals.index(card[0])+1) > maxCardNum:
          maxCardNum = int(vals.index(card[0]))
          maxCard = card
      return maxCard
    else: return winning_card(trick, trick[0][1])
