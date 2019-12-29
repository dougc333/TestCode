def binomial(n,k):
  if k==0:
    return 1
  if (n==k):
    return 1
  return binomial(n-1,k-1) + binomial(n-1,k)

print(binomial(4,2))
print(binomial(5,2)) 
assert(binomial(4,2)==6)
assert binomial(5,2)==10