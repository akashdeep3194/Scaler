from typing import List

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A: List[List]):
        for i in range(len(A)):
            j = 0
            while j< len(A[i]):
                if A[i][j]&1 == 0:
                    j+=1
                else:
                    # A[i].remove(A[i][j])
                    A[i].pop(j)
        return A
# s = Solution()
# A = [  [172222465, 956511006]]

# # A = [ [1, 2, 3, 4],[4, 5, 6, 7], [8, 9, 10, 11], [13, 15, 17, 19] ]
# s.solve(A)
