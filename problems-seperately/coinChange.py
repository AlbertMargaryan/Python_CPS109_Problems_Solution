def give_change(amount, coins):
  tempAmount = amount
  result = []
  for coin in coins:
    while tempAmount  >= coin:
        tempAmount -= coin
        result.append(coin)
  return result


def coin_change_recursive(amount, denominations, memo={}):
  if amount == 0:
      return []

  if amount < 0:
      return None

  if amount in memo:
      return memo[amount]

  best_change = None
  for coin in denominations:
      remaining_amount = amount - coin
      remaining_change = coin_change_recursive(remaining_amount, denominations, memo)

      if remaining_change is not None:
          current_change = [coin] + remaining_change

          if best_change is None or len(current_change) < len(best_change):
              best_change = current_change

  memo[amount] = best_change
  return best_change
