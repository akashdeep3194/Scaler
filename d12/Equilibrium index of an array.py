class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        s = 0
        for ele in A:
            s += ele
        ls = 0
        for i in range(len(A)):
            s = s - A[i]
            if i > 0:
                ls += A[i-1]
            if ls == s:
                return i
        return -1


# s=Solution()
# print(s.solve([-7, 1, 5, 2, -4, 3, 0]))
