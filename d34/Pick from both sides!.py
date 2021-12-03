class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        sm = 0

        for i in range(B):
            sm += A[i]

        ans = sm
        n = len(A)

        for i in range(1,B+1):
            sm = sm - A[B-i] + A[n-i]
            ans = max(sm,ans)
        
        return ans

# s = Solution()
# print(s.solve([5,7, 1, 3, -2, 3 , 1, 35, 2, 5],3))
