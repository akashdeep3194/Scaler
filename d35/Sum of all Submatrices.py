class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        s = 0

        m = len(A)
        n = len(A[0])

        for i in range(len(A)):
            for j in range(len(A[0])):

                s = s + A[i][j]*(m-i)*(n-j)*(i+1)*(j+1)
            
        return s

# s = Solution()
# A = [ [1, 1], [1, 1] ]
# print(s.solve(A))
