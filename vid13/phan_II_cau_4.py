def F(A, n):
  for i in range(1, n):
    x = A[i]
    j = i - 1

    while j >= 0 and A[j] > x:
      A[j + 1] = A[j]
      j = j - 1
    
    A[j + 1] = x
  
  print(A)
  
  return (A[n // 2] + A[n - 1]) / 2

print(F([8, 6, 4, 2, 3, 5, 7], 7))