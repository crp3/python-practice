def knapsack(weights, vals, max_weight, use_memo=True):
  if use_memo:
    return knapsack_helper_memo(weights, vals, max_weight, 0)
  return knapsack_helper(weights, vals, max_weight, 0)

def knapsack_helper_memo(weights, vals, max_weight, i, cache=None):
  if not cache:
    cache = [[-1]*(max_weight+1)]*(len(weights)+1)

  if cache[i][max_weight] != -1:
    return cache[i][max_weight]
  if i == len(vals):
    return 0

  if max_weight - weights[i] < 0:
    cache[i][max_weight] = knapsack_helper_memo(weights, vals, max_weight, i+1, cache)
    return cache[i][max_weight]
  else:
    cache[i][max_weight] = max(
      knapsack_helper_memo(weights, vals, max_weight-weights[i], i+1, cache) + vals[i],
      knapsack_helper_memo(weights, vals, max_weight, i+1, cache)
    )
  return cache[i][max_weight]

def knapsack_helper(weights, vals, max_weight, i):
  if i == len(vals):
    return 0

  if max_weight - weights[i] < 0:
    return knapsack_helper(weights, vals, max_weight, i+1)
  else:
    return max(
      knapsack_helper(weights, vals, max_weight-weights[i], i+1) + vals[i],
      knapsack_helper(weights, vals, max_weight, i+1)
    )

if __name__ == '__main__':
  weights = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27] 
  vals = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
  max_weight = 67

  assert knapsack(weights, vals, max_weight) == 1270
  assert knapsack(weights, vals, max_weight, use_memo=True) == 1270
  
