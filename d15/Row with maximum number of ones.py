class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        i=0
        j=len(A[0])-1
        n = 0

        while(i<len(A) and j>=0):
            if A[i][j] == 1:
                j-=1
                n = i
            else:
                i+=1

        return n

A = [[0, 1, 1],[0, 0, 1],[0, 1, 1]]

s = Solution()
print(s.solve(A))
