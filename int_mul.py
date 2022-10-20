def multiply(p,q):
    n = len(p)
    if(n == 1):        
        return p[0]*q[0]
    else:
        mid = n//2
        U = multiply(p[mid:n+1],q[mid:n+1])
        L = multiply(p[0:mid],q[0:mid])
        for i in range(mid):
            A.append(p[i+mid]+p[i])
            B.append(q[i+mid]+q[i])
            # print(type(A))
        M = multiply(A,B)
        R = [0]*(2*n)
        # print(L)
        # for i in range(len(R[:n-2])+1):
        #     R[i] = R[i]+L
        # for i in range(len(R[(mid):2*mid])):
        #     R[mid+i] = R[mid+i]+M-U-L
        # for i in range(len(R[2*mid:n+1])):
        #     R[2*mid+i] = R[2*mid+i]+U   
        return R
P = [1,1,1]
Q = P
A = []
B=[]
# M=[]
# U = []
# L = []
print(multiply(P,Q))
# print(type(q))