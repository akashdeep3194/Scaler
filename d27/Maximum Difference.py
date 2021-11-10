class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        xs = ns = 0
        ts = 0
        for i in range(B):
            xs += A[i]
        for j in range(len(A)):
            ts += A[j]
        for k in range(len(A)-1,len(A)-B-1,-1):
            ns += A[k]
        return max(abs(2*ns-ts),abs(2*xs-ts))


# A = [ 48, 63 ]
# s = Solution()
# print(s.solve(A,1))
