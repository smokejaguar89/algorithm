def _combos(n, d={}):

  yield [n]

  for x in reversed(xrange(1, n)):
    if n - x == 1:
      yield [x, 1]
    else:
      # If combinations for remainder already calculated (memoisation)
      if n - x in d:
        for y in d[n-x]:
          # Prevents duplicates
          if x >= y[0]:
            yield [x] + y

      # If not yet in dictionary
      else:
        d[n - x] = []
        for y in _combos(n - x):
          # Prevents duplicates
          if x >= y[0]:
            d[n - x].append(y)
            yield [x] + y


def combos(n):
  for x in _combos(n):
    print x

combos(3)
