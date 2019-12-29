def jac_recursion(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return jac_recursion(n-1) + 2*jac_recursion(n-2)

def jac_dp(n):
  a=0
  b=1
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    for i in range(2,n+1):
      c=a+b
      a=2*b
      b=c
    return b


print(jac_recursion(0))
print(jac_dp(0))
print('-----------')
print(jac_recursion(1))
print(jac_dp(1))
print('-----------')
print(jac_recursion(2))
print(jac_dp(2))
print('-----------')
print(jac_recursion(3))
print(jac_dp(3))
print('-----------')
print(jac_recursion(4))
print(jac_dp(4))
print('-----------')
print(jac_recursion(5))
print(jac_dp(5))

print(len(str(jac_dp(241))))