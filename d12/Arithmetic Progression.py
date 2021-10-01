class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        A = sorted(A)
        k = A[0]
        d = A[1]-A[0]

        for i in range(1,len(A)):

            if d*i+k == A[i]:
                continue
            else:
                return 0
        return 1

# s=Solution()

# print(s.solve())
