def words_with_given_shape(words, shape):
  def cmp(a, b):
    return (a < b) - (a > b) 
  def word_to_shape(word):
      return [cmp(ord(word[i]), ord(word[i + 1])) for i in range(len(word) - 1)]
  
  result = []
  for word in words:
    x = word_to_shape(word)
    print(x)
    if x == shape:
        result.append(word)
  
  return result
