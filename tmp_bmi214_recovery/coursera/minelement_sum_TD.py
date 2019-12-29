def minelement(n,S):
  r=[None]*(n+1) 
  print("r:",r)
  a = minelement_aux(n,S,r)
  print("a:",a)
  return a

def minelement_aux(n,S,r):
  print("minelement_aux r:",r," n:",n)
  print("minelement_aux r[n]:",r[n])
  
  if r[n]!=None:
    return r[n]
  if n==0:
    return 0
  elif n<min(S):
    return None

  candidates=[]
  for s in S: 
    cand = minelement_aux(n-s,S,r)
    if cand is not None:
       candidates.append(cand+1)
  if len(candidates) ==0:
    return None
  r[n] = min(candidates)
  return r[n]


print(minelement(0,[5,4,1]))
print(minelement(1,[5,4,1]))
print(minelement(2,[5,4,1]))
print(minelement(3,[5,4,1]))

