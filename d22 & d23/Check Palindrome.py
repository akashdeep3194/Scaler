import sys
sys.setrecursionlimit(10**5)

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        return self.solveh(A,0,len(A)-1)
    

    def solveh(self, A,si,ei):

        if si>=ei:
            return True

        if A[si] == A[ei]:
            sa = self.solveh(A,si+1,ei-1)
            return sa
        else:
            return False

# s = Solution()
# print(s.solve("PallaP"))
