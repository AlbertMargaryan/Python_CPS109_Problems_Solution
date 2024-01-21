def onlyOddDigits(num):
  numString = str(num)
  return all(int(digit) % 2 != 0 for digit in numString)
