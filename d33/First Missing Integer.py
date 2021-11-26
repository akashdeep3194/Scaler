class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i<n:
            if A[i]<=n and A[i]>0 and A[i] != A[A[i]-1]:
                cur = A[i]
                A[i],A[cur-1] = A[cur-1],A[i]
                i -= 1
            i += 1

        expected = 1
        for ele in A:
            if ele != expected:
                return expected
            else:
                expected += 1
        return expected

# s = Solution()
# print(s.firstMissingPositive([3, 4, -1, 1]))
