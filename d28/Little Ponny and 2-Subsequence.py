class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if len(A)<=2:
            return A
        ans = ""
        ans = A[-2] + A[-1]
        m = A[-2]
        n = A[-1]
        for i in range(len(A)-3,-1,-1):
            if A[i]<=m:
                n = min(m,n)
                m = A[i]
                ans = m+n
        return ans

# s = Solution()
# print(s.solve("ksdjgha"))
