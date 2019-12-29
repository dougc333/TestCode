import sys

def minCoins(coins,V):
  m=len(coins)
  lookup=[0]*(V+1)
  for i in range(1,V+1):
    lookup[i] = sys.maxsize
  for i in range(1,V+1):
    for j in range(m):
      if (coins[j]<=i):
        sub_res = lookup[i-coins[j]]
        if (sub_res !=sys.maxsize) and ( (sub_res+1) < lookup[i]):
          lookup[i] = sub_res + 1
  return lookup[V]

coins=[5,4,1]
m = len(coins)
print("0:",minCoins(coins,0))
print("1:",minCoins(coins,1))
print("2:",minCoins(coins,2))
print("3:",minCoins(coins,3))
print("4:",minCoins(coins,4))
print("5:",minCoins(coins,5))
print("6:",minCoins(coins,6))
print("7:",minCoins(coins,7))
print("8:",minCoins(coins,8))
print("9:",minCoins(coins,9))
print("10:",minCoins(coins,10))
print("11:",minCoins(coins,11))
print("12:",minCoins(coins,12))
print("13:",minCoins(coins,13))
print("14:",minCoins(coins,14))
print("15:",minCoins(coins,15))
print("16:",minCoins(coins,16))
print("17:",minCoins(coins,17))
print("18:",minCoins(coins,18))
print("19:",minCoins(coins,19))
print("20:",minCoins(coins,20))
print("21:",minCoins(coins,21))
print("22:",minCoins(coins,22))

