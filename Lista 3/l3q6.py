def BuscaBinaria(A):
  n = len(A)
  e = 0
  d = n - 1
  encontrou = False

  while (e <= d):
    i = (e + d) // 2

    if A[i] == i:
      encontrou = True
      break
    
    if i < A[i]:
      d = i - 1
    
    if i > A[i]:
      e = i + 1
    
  return encontrou