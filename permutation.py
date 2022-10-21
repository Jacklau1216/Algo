A=[1,2]
result =[]    
def permutate(A,l,r):
    if l == r:
        result.append(A[::])
    else:
        for i in range(l,r):
            A[l],A[i] = A[i],A[l]
            permutate(A,l+1,r)
            A[l],A[i] = A[i],A[l]
    return result

print(permutate(A,0,len(A)))
