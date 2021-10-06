class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []

        for j in range(len(A[0])):

            s = 0

            for i in range(len(A)):
                s += A[i][j]
            
            ans.append(s)
        return ans

# s = Solution()

# A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]

# print(s.solve(A))
