def kEsimo(A, B, k):
  n = len(A)
  m = len(B)

  if n == 1 or m == 1:
    if m == 1:
      B, A = A, B
      m = n
    
    if k == 1:
      return min(A[0], B[0])
    
    elif k == m + 1:
      return max(A[0], B[0])
    
    else:
      if B[k - 1] < A[0]:
        return B[k - 1]
      
      else:
        return max(A[0], B[k - 2])
  
  xA = ((n - 1) / 2)
  xB = ((m - 1) / 2)

  if xA + xB + 1 < k:
    if A[xA] < B[xB]:
      return kEsimo(A[xA + 1:], B, k - xA - 1)

    else:
      return kEsimo(A, B[xB + 1:], k - xB - 1)
    
  else:
    if A[xA] > B[xB]:
      return kEsimo(A[:xA + 1], B, k)
    
    else:
      return kEsimo(A, B[:xB + 1], k)