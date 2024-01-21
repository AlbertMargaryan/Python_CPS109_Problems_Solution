def josephus(n, k):
  result = []
  currentRound = list(range(1, n+1))
  currentPerson = 0
  while len(currentRound) != 0:
    currentPerson = (currentPerson + k - 1) % len(currentRound)
    result.append(currentRound[currentPerson])
    del currentRound[currentPerson]
  return result
