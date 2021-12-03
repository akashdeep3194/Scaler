class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        pf = [[0 for _ in range(len(A[0])+1)] for _ in range(len(A)+1)]
        c = 10**9+7
        for i in range(1, len(A)+1):
            for j in range(1,len(A[0])+1):
                pf[i][j] = ((pf[i-1][j]+pf[i][j-1])%c - pf[i-1][j-1] + A[i-1][j-1])%c
        pf.pop(0)
        for ele in pf:
            ele.pop(0)
        
        ans = []
        
        for i in range(len(B)):
            x1 = B[i] - 1
            y1 = C[i] - 1
            x2 = D[i] - 1
            y2 = E[i] - 1
            sm = pf[x2][y2]

            if x1>0:
                sm = (sm - pf[x1-1][y2])%c

            if y1>0:
                sm = (sm - pf[x2][y1-1])%c

            if x1>0 and y1>0:
                sm = (sm + pf[x1-1][y1-1])%c

            ans.append(sm)

        return ans

# s = Solution()

# A = [  [1, 2, 3],  [4, 5, 6],  [7, 8, 9] ]

# B = [ 1, 2 ]
# C = [ 1, 2 ]
# D = [ 2, 3 ]
# E = [ 2, 3 ]

# print(s.solve(A,B,C,D,E))

# 1 2 3
# 4 5 6
# 7 8 9

# 1 3 6
# 4 9 15
# 7 15 24

# 0 0 0 0
# 0 1 3 6
# 0 5 12 21
# 0 12 27 45
