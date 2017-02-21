# Dynamic Programming Example Problem
# Example of using memoisation to save results of already resolved sub-problems

# Recursive approach
def steps_recursive(n, d={}):
  if n < 0:
    return 0
  elif n < 3:
    return n
  else:
    if n in d:
      return d[n]
    else:
      d[n] = steps_recursive(n-1, d) + steps_recursive(n-2, d)
      return d[n]

# Iterative approach
def steps_iterative(n):
  if n < 0:
    return 0
  elif n < 3:
    return n
  else:
    d = { 1: 1, 2: 2 }

    for i in range(3, n+1):
      d[i] = d[i-1] + d[i-2]

    return d[n]

print steps_recursive(50)
print steps_iterative(50)
