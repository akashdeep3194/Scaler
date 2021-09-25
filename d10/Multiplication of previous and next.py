class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        n = len(A)
        if n<2:
            return [0]
        for ind,ele in enumerate(A):
            if ind == 0:
                arr.append(A[ind]*A[ind+1])
            elif ind == n-1:
                arr.append(A[ind]*A[ind-1])
            else:
                arr.append(A[ind-1]*A[ind+1])
        return arr

s = Solution()
print(s.solve([1, 2, 3, 4, 5]))



