def extractIncreasing(digits):
  if digits == "0":
    return [0]
    
  previousDigit = int(digits[0])
  currentDigit = int(digits[1])
  result = [int(digits[0])]
  
  for i, v in enumerate(list(digits)):
    if not(i == 0 or i == len(digits)-1):
      if currentDigit > previousDigit:
        result.append(currentDigit)
        previousDigit = currentDigit
        currentDigit = int(digits[i + 1])
      else:
        currentDigit = currentDigit*10 + int(digits[i+1])
  return result
