def MinElementsSum(n,S):
  if n==0:
    return 0
  elif n<min(S):
    return None
  cand = []
  for s in S:
    c = MinElementsSum(n-s,S)
    if c is not None:
      cand.append(c)
  if len(cand) == 0:
    return None
  return min(cand)

print(MinElementsSum(2,[1,2]))