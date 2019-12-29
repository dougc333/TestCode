recursive_fib(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return recursive_fib(n-1) + recursive_fib(n-2)

cache = {}
cache[0] = 0
cache[1] = 1
def memoized_fib(n):
  if cache.get(n)==None:
    return memoized_fib = memoized_fib(n-1) + memoized_fib(n-2)
  else:
    return cache[n]