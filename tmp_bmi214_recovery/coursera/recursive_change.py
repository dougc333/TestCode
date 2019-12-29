def RecursiveChange(money,Coins):
  if money==0:
    return 0
  MinNumCoins = 10000
  for i in range(0,len(Coins)-1):
    if money >= Coins[i]:
      numcoins=RecursiveChange(money-Coins[i],Coins)
      if numcoins+1 < MinNumCoins:
        MinNumCoins = numcoins+1
  return MinNumCoins

print(RecursiveChange(76,[5,4,1]))
#this is wrong
print(RecursiveChange(12,[5,4,1]))
print(RecursiveChange(11,[5,4,1]))
print(RecursiveChange(10,[5,4,1]))
print(RecursiveChange(9,[5,4,1]))
print(RecursiveChange(8,[5,4,1]))
print(RecursiveChange(7,[5,4,1]))
print(RecursiveChange(6,[5,4,1]))
print(RecursiveChange(5,[5,4,1]))

print(RecursiveChange(4,[5,4,1]))
print(RecursiveChange(3,[5,4,1]))
print(RecursiveChange(2,[5,4,1]))
print(RecursiveChange(1,[5,4,1]))
