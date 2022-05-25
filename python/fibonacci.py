def fibonacci(n):
  
  FibList = [0, 1]

  for i in range(0, n):
    FibList.append(FibList[-1] + FibList[-2])

  return FibList[n]


