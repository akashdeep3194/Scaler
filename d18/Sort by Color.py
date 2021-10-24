class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        n = len(A)

        nonzero = -1

        for i in range(n):
            if A[i] != 0 and nonzero == -1:
                nonzero = i
            if A[i] == 0 and nonzero != -1:
                A[i],A[nonzero] = A[nonzero], A[i]
                nonzero += 1

        firsttwo = -1

        for i in range(n):
            if A[i] == 2 and firsttwo == -1:
                firsttwo = i
                continue
            if A[i] == 1 and firsttwo != -1:
                A[i],A[firsttwo] = A[firsttwo], A[i]
                firsttwo += 1
        return A

# s = Solution()
# A = [2]
# print(s.sortColors(A))
