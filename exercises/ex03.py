'''
def calculate(vec):
  return(sum(vec)/len(vec),max(vec),min(vec),sum(vec))

a,b = 9,8
vec = [1.98,2.45,3.09,4.67,8.54]
avg,maximum,minimum,summation = calculate(vec)

print(avg,maximum,minimum,summation)

# --------exec 3--------------
def fact (n):
  if n == 0: return 1
  else : return (n * fact(n-1))

print(fact(4))

'''
# --------exec 4--------------
def func(i):
  output = dict()
  for v in range(1,i):
      output[v] = v * v 
  return output


print(func(4))

# -------exec 5 ---------
newVec =list( map(lambda v : v*v , range(1,4) ))
print(type(newVec))


print(newVec)

