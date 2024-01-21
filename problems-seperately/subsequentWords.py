def words_with_letters(words, letters):
  result = []

  for word in words:
    tempWord = word
    count = len(letters)

    for letter in letters:
      if tempWord.find(letter) < 0:
        break
      elif tempWord.find(letter) >= 0:
        tempWord = tempWord[int(tempWord.find(letter)) + 1:]
        count -= 1
    if count == 0:
      result.append(word)

  return result
