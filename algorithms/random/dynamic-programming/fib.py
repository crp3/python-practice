from utils import timing_val

@timing_val
def fib(n):
  if n <= 1: return n
  return fib(n-1) + fib(n-2)

@timing_val
def fib_memo(n, memo = {}):
  if n in memo:
    return memo[n]
  if n <= 1: return n
  memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]

if __name__ == '__main__':
  times = []
  times.append(fib(10))
  times.append(fib_memo(10))
  times.append(fib(20))
  times.append(fib_memo(20))
  times.append(fib(30))
  times.append(fib_memo(30))

  for (time, result, func_name) in times:
    print(f'{func_name} took {time*1000}ms.')

